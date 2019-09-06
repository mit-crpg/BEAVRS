"""univzero.py

Provides a container class for the BEAVRS main universe cells

"""

import beavrs.constants as c

import openmc

class UniverseZero(openmc.Universe):

    def __init__(self, core, mats, is_2d=False):
        """ Creates BEAVRS main universe """
        super(UniverseZero, self).__init__(name='Main BEAVRS universe', universe_id=0)

        self.core = core
        self.mats = mats
        self.is_2d = is_2d

        self._add_outer_rings()
        self._add_shield_panels()
        self._add_core_barrel()
        self._create_main_universe()


    def _add_outer_rings(self):
        """ Adds BEAVRS RPV, liner, and downcomer """

        # Change z-dimension based on whether 2D or 3D problem
        if self.is_2d:
            self.s_upperBound = openmc.ZPlane(name='Highest Extent', z0=c.struct_HighestExtent_2d, boundary_type='reflective')
            self.s_lowerBound = openmc.ZPlane(name='Lowest Extent', z0=c.struct_LowestExtent_2d, boundary_type='reflective')
        else:
            self.s_upperBound = openmc.ZPlane(name='Highest Extent', z0=c.struct_HighestExtent, boundary_type='vacuum')
            self.s_lowerBound = openmc.ZPlane(name='Lowest Extent', z0=c.struct_LowestExtent, boundary_type='vacuum')

        # RPV

        self.s_RPVOR = openmc.ZCylinder(name='RPV OR', r=c.rpvOR, boundary_type='vacuum')
        self.s_RPVIR = openmc.ZCylinder(name='RPV IR', r=c.rpvIR)
        self.c_RPV = openmc.Cell(name="RPV", fill=self.mats['Carbon Steel'])
        self.c_RPV.region = (-self.s_RPVOR & +self.s_RPVIR &
                             -self.s_upperBound & +self.s_lowerBound)

        # RPV liner

        self.s_linerIR = openmc.ZCylinder(name='RPV Liner IR', r=c.linerIR)
        self.c_liner = openmc.Cell(name="RPV Liner", fill=self.mats['SS304'])
        self.c_liner.region = (-self.s_RPVIR & +self.s_linerIR &
                               -self.s_upperBound & +self.s_lowerBound)

        # Downcomer

        self.s_neutronShieldOR = openmc.ZCylinder(name='Shield Panel OR', r=c.neutronShieldOR)
        self.c_downcomer = openmc.Cell(name="Downcomer", fill=self.mats['Borated Water'])
        self.c_downcomer.region = (-self.s_linerIR & +self.s_neutronShieldOR &
                               -self.s_upperBound & +self.s_lowerBound)


    def _add_shield_panels(self):
        """ Adds BEAVRS shield panels """

        # Shield panels
        self.s_neutronShieldIR = openmc.ZCylinder(name='Shield Panel IR', r=c.neutronShieldIR)
        self.s_ns_NWbot_SEtop = openmc.Plane(name='Shield Panel NWbot/SEtop', **c.neutronShield_NWbot_SEtop)
        self.s_ns_NWtop_SEbot = openmc.Plane(name='Shield Panel NWtop/SEbot', **c.neutronShield_NWtop_SEbot)
        self.s_ns_NEbot_SWtop = openmc.Plane(name='Shield Panel NEbot/SWtop', **c.neutronShield_NEbot_SWtop)
        self.s_ns_NEtop_SWbot = openmc.Plane(name='Shield Panel NEtop/SWbot', **c.neutronShield_NEtop_SWbot)

        self.c_shieldPanels = []

        self.c_sp_NW = openmc.Cell(name='NW Shield Panel', fill=self.mats['SS304'])
        self.c_sp_NW.region = (+self.s_neutronShieldIR & -self.s_neutronShieldOR &
                               +self.s_ns_NWbot_SEtop & -self.s_ns_NWtop_SEbot &
                               -self.s_upperBound & +self.s_lowerBound)
        self.c_shieldPanels.append(self.c_sp_NW)

        self.c_sp_SE = openmc.Cell(name='SE Shield Panel', fill=self.mats['SS304'])
        self.c_sp_SE.region = (+self.s_neutronShieldIR & -self.s_neutronShieldOR &
                               -self.s_ns_NWbot_SEtop & +self.s_ns_NWtop_SEbot &
                               -self.s_upperBound & +self.s_lowerBound)
        self.c_shieldPanels.append(self.c_sp_SE)

        self.c_sp_NE = openmc.Cell(name='NE Shield Panel', fill=self.mats['SS304'])
        self.c_sp_NE.region = (+self.s_neutronShieldIR & -self.s_neutronShieldOR &
                               +self.s_ns_NEbot_SWtop & -self.s_ns_NEtop_SWbot &
                               -self.s_upperBound & +self.s_lowerBound)
        self.c_shieldPanels.append(self.c_sp_NE)

        self.c_sp_SW = openmc.Cell(name='SW Shield Panel', fill=self.mats['SS304'])
        self.c_sp_SW.region = (+self.s_neutronShieldIR & -self.s_neutronShieldOR &
                               -self.s_ns_NEbot_SWtop & +self.s_ns_NEtop_SWbot &
                               -self.s_upperBound & +self.s_lowerBound)
        self.c_shieldPanels.append(self.c_sp_SW)

        self.c_sp_N = openmc.Cell(name='N Shield Water', fill=self.mats['Borated Water'])
        self.c_sp_N.region = (+self.s_neutronShieldIR & -self.s_neutronShieldOR &
                              +self.s_ns_NWtop_SEbot & -self.s_ns_NEtop_SWbot &
                              -self.s_upperBound & +self.s_lowerBound)
        self.c_shieldPanels.append(self.c_sp_N)

        self.c_sp_S = openmc.Cell(name='S Shield Water', fill=self.mats['Borated Water'])
        self.c_sp_S.region = (+self.s_neutronShieldIR & -self.s_neutronShieldOR &
                              +self.s_ns_NEtop_SWbot & -self.s_ns_NWtop_SEbot &
                              -self.s_upperBound & +self.s_lowerBound)
        self.c_shieldPanels.append(self.c_sp_S)

        self.c_sp_E = openmc.Cell(name='E Shield Water', fill=self.mats['Borated Water'])
        self.c_sp_E.region = (+self.s_neutronShieldIR & -self.s_neutronShieldOR &
                              +self.s_ns_NWbot_SEtop & +self.s_ns_NEbot_SWtop &
                              -self.s_upperBound & +self.s_lowerBound)
        self.c_shieldPanels.append(self.c_sp_E)

        self.c_sp_W = openmc.Cell(name='W Shield Water', fill=self.mats['Borated Water'])
        self.c_sp_W.region = (+self.s_neutronShieldIR & -self.s_neutronShieldOR &
                              -self.s_ns_NWbot_SEtop & -self.s_ns_NEbot_SWtop &
                              -self.s_upperBound & +self.s_lowerBound)
        self.c_shieldPanels.append(self.c_sp_W)

        self.s_coreBarrelOR = openmc.ZCylinder(name='Core Barrel OR', r=c.coreBarrelOR)
        self.c_sp_inner = openmc.Cell(name='Water between barrel and shield', fill=self.mats['Borated Water'])
        self.c_sp_inner.region = (+self.s_coreBarrelOR & -self.s_neutronShieldIR &
                                  -self.s_upperBound & +self.s_lowerBound)
        self.c_shieldPanels.append(self.c_sp_inner)


    def _add_core_barrel(self):
        """ Adds BEAVRS core barrel and core lattice """

        # Core barrel

        self.s_coreBarrelIR = openmc.ZCylinder(name='Core Barrel IR', r=c.coreBarrelIR)
        self.c_coreBarrel = openmc.Cell(name="Core Barrel", fill=self.mats['SS304'])
        self.c_coreBarrel.region = (-self.s_coreBarrelOR & +self.s_coreBarrelIR &
                                    -self.s_upperBound & +self.s_lowerBound)

        # Core lattice

        self.c_core = openmc.Cell(name="Core lattice", fill=self.core.u_coreLattice)
        self.c_core.region = \
            (-self.s_coreBarrelIR & -self.s_upperBound & +self.s_lowerBound)


    def _create_main_universe(self):
        """ Creates the main BEAVRS universe """

        # For 3D problem, add full core to main universe
        if not self.is_2d:
            self.add_cell(self.c_RPV)
            self.add_cell(self.c_liner)
            self.add_cell(self.c_downcomer)
            for cell in self.c_shieldPanels: self.add_cell(cell)
            self.add_cell(self.c_coreBarrel)
            self.add_cell(self.c_core)

       # For 2D problem, create core universe separately and set bounding box as main universe
        else:
            # Define core universe that will be fill of main universe
            self.core_univ = openmc.Universe(name='BEAVRS core universe')
            self.core_univ.add_cell(self.c_RPV)
            self.core_univ.add_cell(self.c_liner)
            self.core_univ.add_cell(self.c_downcomer)
            for cell in self.c_shieldPanels: self.core_univ.add_cell(cell)
            self.core_univ.add_cell(self.c_coreBarrel)
            self.core_univ.add_cell(self.c_core)

            # Define boundaries of bounding box
            outer_bound = 8.5*c.latticePitch
            self.s_leftBound = openmc.XPlane(name='Left Box', x0=-outer_bound, boundary_type='vacuum')
            self.s_rightBound = openmc.XPlane(name='Right Box', x0=outer_bound, boundary_type='vacuum')
            self.s_backBound = openmc.YPlane(name='Back Box', y0=-outer_bound, boundary_type='vacuum')
            self.s_frontBound = openmc.YPlane(name='Front Box', y0=outer_bound, boundary_type='vacuum')

            # Bounding box

            self.c_boundbox = openmc.Cell(name="Bounding box", fill=self.core_univ)
            self.c_boundbox.region = \
                (+self.s_leftBound & -self.s_rightBound &
                 +self.s_backBound & -self.s_frontBound &
                 -self.s_upperBound & +self.s_lowerBound)

            self.add_cell(self.c_boundbox)
