""" corebuilder.py

This module provides several classes that facilitate easier modeling of LWRs
with OpenMC

"""

import openmc


class TemplatedLattice(openmc.RectLattice):
    """Extends OpenMC lattices for setting universes in a templated fashion"""

    def __init__(self, *args, **kwargs):
        super(TemplatedLattice, self).__init__(*args, **kwargs)
        self.positions = {}
        self.template = []

    def setTemplate(self, template):
        """ Set the lattice template

        :param template:
        """
        self.template = template

    def setPosition(self, key, univ):
        """Set an individual position in the lattice"""
        self.positions[key] = univ

    def updatePositions(self, univs):
        """Update multiple positions in the lattice with a dictionary"""
        self.positions.update(univs)

    def finalize(self):

        if self.template == []:
            raise Exception("No template set for:\n{0}".format(self))

        universes = []
        for row in self.template:
            r = []
            for item in row:
                try:
                    r.append(self.positions[item.strip()])
                except KeyError:
                    raise Exception("Must set template position '{0}' for template " +\
                                    " in:\n{1}".format(item.strip(), self))
            universes.append(r)
        self.universes = universes


_created_cells = {}


class InfinitePinCell(openmc.Universe):
    """ Class for creating a simple pincell universe infinite in the z direction

    InfinitePinCells consist of a set of radii and materials that define rings.

    This class provides an easy way to wrap a pincell inside additional rings, or
    a square grid around the outside.

    """

    def __init__(self, *args, **kwargs):
        """ Create a new InfinitePinCell
        """
        super(InfinitePinCell, self).__init__(*args, **kwargs)
        self.radii = []
        self.box = []
        self.fills = []
        self.rot = []
        self.finalized = False

    def add_ring(self, fill, surf, box=False, rot=None):
        """ Adds a ring to the pincell

        Pincells must be built from the inside out. Materials for new rings are from
        the surface of the previous ring to the provided new surface.

        If the ring we want to add is a box, surf should be a rectangular prism.

        It's up to the user to check for overlapping cell definitions.

        :param fill: material or filling universe for new ring
        :param surf: outer surface of new ring (or a rectangular region)
        :param box: whether or not we're adding a boxy ring (e.g. for grids)
        :param rot: openmc rotation string for filled cells

        """
        self.radii.append(surf)
        self.box.append(box)
        self.fills.append(fill)
        self.rot.append(rot)

    def add_last_ring(self, fill, rot=None):
        """ Adds the outermost cell in the pincell that goes to infinity

        :param fill: material or filling universe for outermost region

        """
        self.fills.append(fill)
        self.rot.append(rot)

    def finalize(self):
        """ Creates Cell objects according to the pincell specification"""

        if self.finalized:
            return

        ## Loop over each ring and add cells for inner rings
        params = zip(self.radii, self.box, self.fills, self.rot)
        for i, (radius, box, fill, rot) in enumerate(params):

            label = "{0} radial {1}: {2}".format(self._name, i, fill._name)

            if i == 0:
                # this is the first ring

                if box:
                    # this first ring is a box ring

                    cell = openmc.Cell(name=label, fill=fill)
                    cell.region = radius
                    if not rot is None: cell.rotation = rot
                    self.add_cell(cell)

                else:
                    # this first ring is a regular cylinder

                    cell = openmc.Cell(name=label, fill=fill)
                    cell.region = -radius
                    if not rot is None: cell.rotation = rot
                    self.add_cell(cell)

            else:
                # this is not the first ring

                if self.box[i-1]:
                    # the last ring was a box

                    if box:
                        # this is a box ring, and the last one was also a box ring
                        cell = openmc.Cell(name=label, fill=fill)
                        cell.region = ~radius
                        if not rot is None: cell.rotation = rot
                        self.add_cell(cell)

                    else:
                        # this is a regular cylinder, and the last one was a box ring
                        cell = openmc.Cell(name=label, fill=fill)
                        cell.region = -r & ~self.radii[i-1]
                        self.add_cell(cell)

                else:
                    # the last ring was a regular cylinder

                    if box:
                        # this is a box ring, and the last one was a regular cylinder

                        cell = openmc.Cell(name=label, fill=fill)
                        cell.region = +self.radii[i-1] & radius
                        if not rot is None: cell.rotation = rot
                        self.add_cell(cell)

                    else:
                        # this is a regular ring, and the last one was a regular cylinder

                        cell = openmc.Cell(name=label, fill=fill)
                        cell.region = +self.radii[i-1] & -radius
                        if not rot is None: cell.rotation = rot
                        self.add_cell(cell)

        ## Now write the outermost cell(s) that go to infinity

        label = "{0} radial outer: {1}".format(self._name, self.fills[-1]._name)

        if self.box[-1]:
            # the last one is a box, we need 4 outer cells to infinity
            cell = openmc.Cell(name=label, fill=self.fills[-1])
            cell.region = ~radius
            if not self.rot[-1] is None: cell.rotation = self.rot[-1]
            self.add_cell(cell)

        else:

            # the last one is a regular cylindrical ring - just one cell to infinity
            cell = openmc.Cell(name=label, fill=self.fills[-1])
            cell.region = +self.radii[-1]
            if not self.rot[-1] is None: cell.rotation = self.rot[-1]
            self.add_cell(cell)

        self.finalized = True


class AxialPinCell(openmc.Universe):
    """ Class for containing a complete axial description of a pincell

    AxialPinCells consist of a set of InfinitePincells and the axial planes that
    define the axial boundaries of each.  They also allow for a fully-constructed
    pincell to be "wrapped" by another pincell, e.g., pincells containing grids or
    guide tubes.

    """

    def __init__(self, *args, **kwargs):
        """ Create a new AxialPinCell"""

        super(AxialPinCell, self).__init__(*args, **kwargs)
        self.axials = []
        self.pincells = []
        self.finalized = False
        self.outermost = None

    def add_axial_section(self, axial_plane, pincell):
        """ Adds an axial section to the stack

        Stacks must be built from the bottom-up. Each new section goes from the
        previous axial_plane to the given axial_plane (or from infinity to the
        given plane if it's the first section added).

        It's up to the user to ensure that all planes are z-planes, and that
        sections are added in the correct order.

        A call to add_last_axial_section must be made to add the top-most section.

        :param axial_plane: Axial surface above which to add the new pincell
        :param pincell: InfinitePincell or material to add to the top of the stack

        """
        self.axials.append(axial_plane)
        self.pincells.append(pincell)
        if isinstance(pincell, InfinitePinCell):
            self.compare_outermost(pincell)

    def add_last_axial_section(self, pincell):
        """ Adds the last axial section to the top of the stack

        :param pincell: InfinitePincell or material that goes to infinity at the top

        """
        self.pincells.append(pincell)
        if isinstance(pincell, InfinitePinCell):
            self.compare_outermost(pincell)

    def compare_outermost(self, pincell):
        """ Finds if the pincell has the largest outer radius amongst all sections"""
        if not self.outermost:
            self.outermost = pincell
        else:
            if isinstance(self.outermost.radii[-1], openmc.ZCylinder):
                # current is a cylinder
                current = self.outermost.radii[-1].coefficients['r']
            else:
                # current is a box
                current = self.outermost.radii[-1][-1]._surface.y0
            if isinstance(pincell.radii[-1], openmc.ZCylinder):
                # new one is a cylinder
                new = pincell.radii[-1].coefficients['r']
            else:
                # new one is a box
                new = self.outermost.radii[-1][-1]._surface.y0
            if new > current:
                self.outermost = pincell

    def add_wrapper(self, wrapper, surf=None):
        """ Adds a pincell to wrap the height, returning a new InfinitePinCell

        This should only be called AFTER all axial sections are added.

        If the splitting surface is not given, this function will use the outer-most
        radius amongst all pincells in the wrappee to form the ring of the new
        InfinitePincell. It's up to the user to make sure all radii of the outer
        pin are larger than this radius, otherwise cells in the wrapper may be clipped.

        :param wrapper: Another InfinitePinCell or AxialPinCell to wrap this pincell
        :param surf: Splitting surface of new ring

        """

        if self == wrapper:
            return self

        new_name = "({0}) wrapped by ({1})".format(self._name, wrapper._name)

        if new_name in _created_cells:
            return _created_cells[new_name]

        # Finalize the current pincell
        self.finalize()

        # Make a new pincell
        new_pin = InfinitePinCell(name=new_name)

        # If splitting surface is not given, use the outermost radius
        box = False
        rot = None
        if surf is None:
            pin = self.outermost
            surf = pin.radii[-1]
            box = pin.box[-1]
            rot = pin.rot[-1]

        # Fill the inner ring with the wrapped universe
        new_pin.add_ring(self, surf, box=box, rot=rot)

        # Fill the outermost ring with the wrapping universe
        new_pin.add_last_ring(wrapper)

        _created_cells[new_name] = new_pin

        return new_pin

    def finalize(self):
        """ Creates the Cells for this universe"""

        if self.finalized:
            return

        # Instantiate radial cells
        for pin in self.pincells:
            if isinstance(pin, InfinitePinCell) and not pin.finalized:
                pin.finalize()

        # Instantiate the axial cells
        for i, (pin, plane) in enumerate(zip(self.pincells, self.axials)):

            label = "{0} axial {1}: {2}".format(self.name, i, pin.name)
            cell = openmc.Cell(name=label, fill=pin)

            if i == 0:
                # Bottom section
                cell.region = -plane

            else:
                # Middle section
                cell.region = -plane & +self.axials[i-1]

            self.add_cell(cell)

        # Top section
        label = "{0} axial top: {1}".format(self.name, self.pincells[-1].name)
        cell = openmc.Cell(name=label, fill=self.pincells[-1])
        cell.region = +self.axials[-1]

        self.add_cell(cell)

        self.finalized = True
