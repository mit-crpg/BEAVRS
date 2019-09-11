"""lattices.py

Provides a container class of all BEAVRS lattices

"""

import openmc

import beavrs.constants as c
from beavrs.corebuilder import TemplatedLattice
from beavrs.corebuilder import InfinitePinCell

class Assemblies(object):

    pin_lattice_template = [
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', '   a', 'fuel', 'fuel', '     b', 'fuel', 'fuel', '   c', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', '   d', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', '   e', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', '   f', 'fuel', 'fuel', '   g', 'fuel', 'fuel', '     h', 'fuel', 'fuel', '   i', 'fuel', 'fuel', '   j', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', '   k', 'fuel', 'fuel', '   l', 'fuel', 'fuel', 'center', 'fuel', 'fuel', '   n', 'fuel', 'fuel', '   o', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', '   p', 'fuel', 'fuel', '   q', 'fuel', 'fuel', '     r', 'fuel', 'fuel', '   s', 'fuel', 'fuel', '   t', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', '   u', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', '   v', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', '   w', 'fuel', 'fuel', '     x', 'fuel', 'fuel', '   y', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel'],
        ['fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', '  fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel', 'fuel']
    ]

    def __init__(self, pincells, mats):
        """ Creates BEAVRS pincell universes """

        self.pins = pincells
        self.mats = mats

        self._add_lattice_surfs()
        self._add_assembly_surfs()
        self._add_bpra_layouts()
        self._add_rcca_layouts()
        self._add_all_assembly_combinations()


    def _add_lattice_surfs(self):
        """ Adds BEAVRS lattice surfaces """

        # Rectangular prism around the edge of the pinlattice
        self.lattice_surfs = \
            openmc.rectangular_prism(17*c.pinPitch, 17*c.pinPitch)


    def _add_assembly_surfs(self):
        """ Adds BEAVRS assebly surfaces - these include the assembly pitch"""

        # Rectangular prism around the edge of the pinlattice
        self.assem_surfs = \
            openmc.rectangular_prism(c.latticePitch, c.latticePitch)


    def _add_bpra_layouts(self):
        """ Adds BEAVRS BPRA layouts """

        self.ba_specs = []

        u_gt = self.pins.u_gt
        u_bp = self.pins.u_bp

        self.ba_specs.append(('no BAs',{
                      'a': u_gt,  'b': u_gt,  'c': u_gt,
                'd': u_gt,                          'e': u_gt,
          'f': u_gt,  'g': u_gt,  'h': u_gt,  'i': u_gt,  'j': u_gt,
          'k': u_gt,  'l': u_gt,              'n': u_gt,  'o': u_gt,
          'p': u_gt,  'q': u_gt,  'r': u_gt,  's': u_gt,  't': u_gt,
                'u': u_gt,                          'v': u_gt,
                      'w': u_gt,  'x': u_gt,  'y': u_gt,
        }))

        self.ba_specs.append(('4',{
                      'a': u_gt,  'b': u_gt,  'c': u_gt,
                'd': u_bp,                          'e': u_bp,
          'f': u_gt,  'g': u_gt,  'h': u_gt,  'i': u_gt,  'j': u_gt,
          'k': u_gt,  'l': u_gt,              'n': u_gt,  'o': u_gt,
          'p': u_gt,  'q': u_gt,  'r': u_gt,  's': u_gt,  't': u_gt,
                'u': u_bp,                          'v': u_bp,
                      'w': u_gt,  'x': u_gt,  'y': u_gt,
        }))

        self.ba_specs.append(('6N',{
                      'a': u_bp,  'b': u_gt,  'c': u_bp,
                'd': u_bp,                          'e': u_bp,
          'f': u_bp,  'g': u_gt,  'h': u_gt,  'i': u_gt,  'j': u_bp,
          'k': u_gt,  'l': u_gt,              'n': u_gt,  'o': u_gt,
          'p': u_gt,  'q': u_gt,  'r': u_gt,  's': u_gt,  't': u_gt,
                'u': u_gt,                          'v': u_gt,
                      'w': u_gt,  'x': u_gt,  'y': u_gt,
        }))

        self.ba_specs.append(('6S',{
                      'a': u_gt,  'b': u_gt,  'c': u_gt,
                'd': u_gt,                          'e': u_gt,
          'f': u_gt,  'g': u_gt,  'h': u_gt,  'i': u_gt,  'j': u_gt,
          'k': u_gt,  'l': u_gt,              'n': u_gt,  'o': u_gt,
          'p': u_bp,  'q': u_gt,  'r': u_gt,  's': u_gt,  't': u_bp,
                'u': u_bp,                          'v': u_bp,
                      'w': u_bp,  'x': u_gt,  'y': u_bp,
        }))

        self.ba_specs.append(('6E',{
                      'a': u_gt,  'b': u_gt,  'c': u_bp,
                'd': u_gt,                          'e': u_bp,
          'f': u_gt,  'g': u_gt,  'h': u_gt,  'i': u_gt,  'j': u_bp,
          'k': u_gt,  'l': u_gt,              'n': u_gt,  'o': u_gt,
          'p': u_gt,  'q': u_gt,  'r': u_gt,  's': u_gt,  't': u_bp,
                'u': u_gt,                          'v': u_bp,
                      'w': u_gt,  'x': u_gt,  'y': u_bp,
        }))

        self.ba_specs.append(('6W',{
                      'a': u_bp,  'b': u_gt,  'c': u_gt,
                'd': u_bp,                          'e': u_gt,
          'f': u_bp,  'g': u_gt,  'h': u_gt,  'i': u_gt,  'j': u_gt,
          'k': u_gt,  'l': u_gt,              'n': u_gt,  'o': u_gt,
          'p': u_bp,  'q': u_gt,  'r': u_gt,  's': u_gt,  't': u_gt,
                'u': u_bp,                          'v': u_gt,
                      'w': u_bp,  'x': u_gt,  'y': u_gt,
        }))

        self.ba_specs.append(('8',{
                      'a': u_gt,  'b': u_gt,  'c': u_gt,
                'd': u_bp,                          'e': u_bp,
          'f': u_gt,  'g': u_gt,  'h': u_bp,  'i': u_gt,  'j': u_gt,
          'k': u_gt,  'l': u_bp,              'n': u_bp,  'o': u_gt,
          'p': u_gt,  'q': u_gt,  'r': u_bp,  's': u_gt,  't': u_gt,
                'u': u_bp,                          'v': u_bp,
                      'w': u_gt,  'x': u_gt,  'y': u_gt,
        }))

        self.ba_specs.append(('12',{
                      'a': u_bp,  'b': u_gt,  'c': u_bp,
                'd': u_bp,                          'e': u_bp,
          'f': u_bp,  'g': u_gt,  'h': u_gt,  'i': u_gt,  'j': u_bp,
          'k': u_gt,  'l': u_gt,              'n': u_gt,  'o': u_gt,
          'p': u_bp,  'q': u_gt,  'r': u_gt,  's': u_gt,  't': u_bp,
                'u': u_bp,                          'v': u_bp,
                      'w': u_bp,  'x': u_gt,  'y': u_bp,
        }))


        self.ba_specs.append(('15NW',{
                      'a': u_bp,  'b': u_bp,  'c': u_bp,
                'd': u_bp,                          'e': u_gt,
          'f': u_bp,  'g': u_bp,  'h': u_bp,  'i': u_bp,  'j': u_gt,
          'k': u_bp,  'l': u_bp,              'n': u_bp,  'o': u_gt,
          'p': u_bp,  'q': u_bp,  'r': u_bp,  's': u_bp,  't': u_gt,
                'u': u_gt,                          'v': u_gt,
                      'w': u_gt,  'x': u_gt,  'y': u_gt,
        }))

        self.ba_specs.append(('15NE',{
                      'a': u_bp,  'b': u_bp,  'c': u_bp,
                'd': u_gt,                          'e': u_bp,
          'f': u_gt,  'g': u_bp,  'h': u_bp,  'i': u_bp,  'j': u_bp,
          'k': u_gt,  'l': u_bp,              'n': u_bp,  'o': u_bp,
          'p': u_gt,  'q': u_bp,  'r': u_bp,  's': u_bp,  't': u_bp,
                'u': u_gt,                          'v': u_gt,
                      'w': u_gt,  'x': u_gt,  'y': u_gt,
        }))

        self.ba_specs.append(('15SW',{
                      'a': u_gt,  'b': u_gt,  'c': u_gt,
                'd': u_gt,                          'e': u_gt,
          'f': u_bp,  'g': u_bp,  'h': u_bp,  'i': u_bp,  'j': u_gt,
          'k': u_bp,  'l': u_bp,              'n': u_bp,  'o': u_gt,
          'p': u_bp,  'q': u_bp,  'r': u_bp,  's': u_bp,  't': u_gt,
                'u': u_bp,                          'v': u_gt,
                      'w': u_bp,  'x': u_bp,  'y': u_bp,
        }))

        self.ba_specs.append(('15SE',{
                      'a': u_gt,  'b': u_gt,  'c': u_gt,
                'd': u_gt,                          'e': u_gt,
          'f': u_gt,  'g': u_bp,  'h': u_bp,  'i': u_bp,  'j': u_bp,
          'k': u_gt,  'l': u_bp,              'n': u_bp,  'o': u_bp,
          'p': u_gt,  'q': u_bp,  'r': u_bp,  's': u_bp,  't': u_bp,
                'u': u_gt,                          'v': u_bp,
                      'w': u_bp,  'x': u_bp,  'y': u_bp,
        }))

        self.ba_specs.append(('16',{
                      'a': u_bp,  'b': u_bp,  'c': u_bp,
                'd': u_bp,                          'e': u_bp,
          'f': u_bp,  'g': u_gt,  'h': u_gt,  'i': u_gt,  'j': u_bp,
          'k': u_bp,  'l': u_gt,              'n': u_gt,  'o': u_bp,
          'p': u_bp,  'q': u_gt,  'r': u_gt,  's': u_gt,  't': u_bp,
                'u': u_bp,                          'v': u_bp,
                      'w': u_bp,  'x': u_bp,  'y': u_bp,
        }))

        self.ba_specs.append(('20',{
                      'a': u_bp,  'b': u_bp,  'c': u_bp,
                'd': u_bp,                          'e': u_bp,
          'f': u_bp,  'g': u_bp,  'h': u_gt,  'i': u_bp,  'j': u_bp,
          'k': u_bp,  'l': u_gt,              'n': u_gt,  'o': u_bp,
          'p': u_bp,  'q': u_bp,  'r': u_gt,  's': u_bp,  't': u_bp,
                'u': u_bp,                          'v': u_bp,
                      'w': u_bp,  'x': u_bp,  'y': u_bp,
        }))


    def _add_rcca_layouts(self):
        """ Adds BEAVRS RCCA layouts """

        self.cr_specs = []
        for bank_label, u_b in sorted(self.pins.u_rcca.items()):
            self.cr_specs.append(("RCCA {0}".format(bank_label),{
                      'a':  u_b,  'b':  u_b,  'c':  u_b,
                'd':  u_b,                          'e':  u_b,
          'f':  u_b,  'g':  u_b,  'h':  u_b,  'i':  u_b,  'j':  u_b,
          'k':  u_b,  'l':  u_b,              'n':  u_b,  'o':  u_b,
          'p':  u_b,  'q':  u_b,  'r':  u_b,  's':  u_b,  't':  u_b,
                'u':  u_b,                          'v':  u_b,
                      'w':  u_b,  'x':  u_b,  'y':  u_b,
          }))


    def _add_all_assembly_combinations(self):
        """ Adds all BEAVRS assembly layouts

        Here we make every possible combination of enrichments, control and shutdown
        banks, with or without instrument tubes.

        """

        types_fuel = self.pins.enrichments
        types_gt = self.ba_specs + self.cr_specs
        types_instr = [(self.pins.u_it_nt,'no instr'), (self.pins.u_it,'instr')]

        self.u_fuel = {}
        self.u_fuel_no_sleeve = {}
        for enr in types_fuel:

            self.u_fuel[enr] = {}
            self.u_fuel_no_sleeve[enr] = {}
            for gt_label, gt_spec in types_gt:

                self.u_fuel[enr][gt_label] = {}
                self.u_fuel_no_sleeve[enr][gt_label] = {}
                for u_c, center_label in types_instr:

                    name = 'Fuel {0} enr {1} {2}'.format(enr, center_label, gt_label)

                    # Make the pin lattice
                    lattice = TemplatedLattice(name=name)
                    lattice.setTemplate(self.pin_lattice_template)
                    lattice.pitch = [c.pinPitch, c.pinPitch]
                    lattice.lower_left = [-17.*c.pinPitch/2., -17.*c.pinPitch/2.]
                    lattice.setPosition('center', u_c)
                    lattice.setPosition('fuel', self.pins.u_fuel_p[enr])
                    lattice.updatePositions(gt_spec)
                    lattice.finalize()

                    # Wrap the lattice with the grid sleeve universe
                    u_lattice = InfinitePinCell(name='{0} universe'.format(name))
                    u_lattice.add_ring(lattice, self.lattice_surfs, box=True)
                    u_lattice.add_last_ring(self.pins.u_gridsleeve)
                    self.u_fuel[enr][gt_label][center_label] = u_lattice
                    u_lattice.finalize()

                    # Store the lattice without the gridsleeve
                    u_latticePins = InfinitePinCell(name='{0} pins'.format(name))
                    u_latticePins.add_ring(lattice, self.lattice_surfs, box=True)
                    u_latticePins.add_last_ring(self.mats['Borated Water'])
                    self.u_fuel_no_sleeve[enr][gt_label][center_label] = u_latticePins
                    u_latticePins.finalize()
