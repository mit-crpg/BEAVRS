"""pincells.py

Provides a container class of all BEAVRS pincells

"""

import openmc

import beavrs.constants as c
from beavrs.corebuilder import InfinitePinCell
from beavrs.corebuilder import AxialPinCell


class Pincells(object):

    def __init__(self, mats):
        """ Creates BEAVRS pincell universes """

        self.mats = mats

        self._add_structural_axials()
        self._add_dummy_universe()
        self._add_grid_pincells()
        self._add_fuel_pincells()
        self._add_guide_tube_pincells()
        self._add_instrument_tube_pincells()
        self._add_bpra_pincells()
        self._add_rcca_pincells()

    def _add_structural_axials(self):
        """ Adds structure axial surfaces common for most pincells """

        self.s_struct_supportPlate_bot = openmc.ZPlane(name='Support plate bottom', z0=c.struct_SupportPlate_bot)
        self.s_struct_supportPlate_top = openmc.ZPlane(name='Support plate top', z0=c.struct_SupportPlate_top)
        self.s_struct_lowerNozzle_bot = openmc.ZPlane(name='Lower nozzle bottom', z0=c.struct_LowerNozzle_bot)
        self.s_struct_lowerNozzle_top = openmc.ZPlane(name='Lower nozzle top', z0=c.struct_LowerNozzle_top)
        self.s_struct_upperNozzle_bot = openmc.ZPlane(name='Upper nozzle bottom', z0=c.struct_UpperNozzle_bot)
        self.s_struct_upperNozzle_top = openmc.ZPlane(name='Upper nozzle top', z0=c.struct_UpperNozzle_top)

    def _add_dummy_universe(self):
        """ Adds all-water universe for empty lattice positions"""

        self.u_waterPin = openmc.Universe(name='Dummy Water Universe')
        self.c_water = openmc.Cell(name='Water', fill=self.mats['Borated Water'])
        self.u_waterPin.add_cells([self.c_water])

    def _add_grid_pincells(self):
        """ Adds BEAVRS pincellgrid and assembly gridsleeve pincells """

        # Rectangular prisms for grid spacers
        grid_surfs_tb = \
            openmc.rectangular_prism(c.rodGridSide_tb, c.rodGridSide_tb)
        grid_surfs_i = \
            openmc.rectangular_prism(c.rodGridSide_i, c.rodGridSide_i)

        # Rectangular prisms for lattice grid sleeves
        grid_surfs_ass = \
            openmc.rectangular_prism(c.gridstrapSide, c.gridstrapSide)

        # Grids axial surfaces

        self.s_grid1_bot = openmc.ZPlane(name='Bottom of grid 1', z0=c.grid1_bot)
        self.s_grid1_top = openmc.ZPlane(name='Top of grid 1',    z0=c.grid1_top)
        self.s_grid2_bot = openmc.ZPlane(name='Bottom of grid 2', z0=c.grid2_bot)
        self.s_grid2_top = openmc.ZPlane(name='Top of grid 2',    z0=c.grid2_top)
        self.s_grid3_bot = openmc.ZPlane(name='Bottom of grid 3', z0=c.grid3_bot)
        self.s_grid3_top = openmc.ZPlane(name='Top of grid 3',    z0=c.grid3_top)
        self.s_grid4_bot = openmc.ZPlane(name='Bottom of grid 4', z0=c.grid4_bot)
        self.s_grid4_top = openmc.ZPlane(name='Top of grid 4',    z0=c.grid4_top)
        self.s_grid5_bot = openmc.ZPlane(name='Bottom of grid 5', z0=c.grid5_bot)
        self.s_grid5_top = openmc.ZPlane(name='Top of grid 5',    z0=c.grid5_top)
        self.s_grid6_bot = openmc.ZPlane(name='Bottom of grid 6', z0=c.grid6_bot)
        self.s_grid6_top = openmc.ZPlane(name='Top of grid 6',    z0=c.grid6_top)
        self.s_grid7_bot = openmc.ZPlane(name='Bottom of grid 7', z0=c.grid7_bot)
        self.s_grid7_top = openmc.ZPlane(name='Top of grid 7',    z0=c.grid7_top)
        self.s_grid8_bot = openmc.ZPlane(name='Bottom of grid 8', z0=c.grid8_bot)
        self.s_grid8_top = openmc.ZPlane(name='Top of grid 8',    z0=c.grid8_top)

        # Grids pincell universes

        self.u_grid_i = InfinitePinCell(name='Intermediate grid pincell')
        self.u_grid_i.add_ring(self.mats['Borated Water'], grid_surfs_i, box=True)
        self.u_grid_i.add_last_ring(self.mats['Zircaloy 4'])
        self.u_grid_i.finalize()

        self.u_grid_tb = InfinitePinCell(name='Top/Bottom grid pincell')
        self.u_grid_tb.add_ring(self.mats['Borated Water'], grid_surfs_tb, box=True)
        self.u_grid_tb.add_last_ring(self.mats['Inconel 718'])
        self.u_grid_tb.finalize()

        self.u_grid_sleeve_i = InfinitePinCell(name='Intermediate grid sleeve pincell')
        self.u_grid_sleeve_i.add_ring(self.mats['Zircaloy 4'], grid_surfs_ass, box=True)
        self.u_grid_sleeve_i.add_last_ring(self.mats['Borated Water'])
        self.u_grid_sleeve_i.finalize()

        self.u_grid_sleeve_tb = InfinitePinCell(name='Top/Bottom grid sleeve pincell')
        self.u_grid_sleeve_tb.add_ring(     self.mats['Inconel 718'], grid_surfs_ass, box=True)
        self.u_grid_sleeve_tb.add_last_ring(self.mats['Borated Water'])
        self.u_grid_sleeve_tb.finalize()

        # Grids axial stack

        self.u_grids = AxialPinCell(name='Grids axial universe')
        self.u_grids.add_axial_section(self.s_struct_supportPlate_bot, self.mats['Borated Water'])
        self.u_grids.add_axial_section(self.s_struct_lowerNozzle_top, self.mats['Water SPN'])
        self.u_grids.add_axial_section(self.s_grid1_bot, self.mats['Borated Water'])
        self.u_grids.add_axial_section(self.s_grid1_top, self.u_grid_tb)
        self.u_grids.add_axial_section(self.s_grid2_bot, self.mats['Borated Water'])
        self.u_grids.add_axial_section(self.s_grid2_top, self.u_grid_i)
        self.u_grids.add_axial_section(self.s_grid3_bot, self.mats['Borated Water'])
        self.u_grids.add_axial_section(self.s_grid3_top, self.u_grid_i)
        self.u_grids.add_axial_section(self.s_grid4_bot, self.mats['Borated Water'])
        self.u_grids.add_axial_section(self.s_grid4_top, self.u_grid_i)
        self.u_grids.add_axial_section(self.s_grid5_bot, self.mats['Borated Water'])
        self.u_grids.add_axial_section(self.s_grid5_top, self.u_grid_i)
        self.u_grids.add_axial_section(self.s_grid6_bot, self.mats['Borated Water'])
        self.u_grids.add_axial_section(self.s_grid6_top, self.u_grid_i)
        self.u_grids.add_axial_section(self.s_grid7_bot, self.mats['Borated Water'])
        self.u_grids.add_axial_section(self.s_grid7_top, self.u_grid_i)
        self.u_grids.add_axial_section(self.s_grid8_bot, self.mats['Borated Water'])
        self.u_grids.add_axial_section(self.s_grid8_top, self.u_grid_tb)
        self.u_grids.add_axial_section(self.s_struct_upperNozzle_bot, self.mats['Borated Water'])
        self.u_grids.add_axial_section(self.s_struct_upperNozzle_top, self.mats['Water SPN'])
        self.u_grids.add_last_axial_section(self.mats['Borated Water'])
        self.u_grids.finalize()

        self.u_gridsleeve = AxialPinCell(name='Grid sleeve axial universe')
        self.u_gridsleeve.add_axial_section(self.s_struct_supportPlate_bot, self.mats['Borated Water'])
        self.u_gridsleeve.add_axial_section(self.s_struct_lowerNozzle_top, self.mats['Water SPN'])
        self.u_gridsleeve.add_axial_section(self.s_grid1_bot, self.mats['Borated Water'])
        self.u_gridsleeve.add_axial_section(self.s_grid1_top, self.u_grid_sleeve_tb)
        self.u_gridsleeve.add_axial_section(self.s_grid2_bot, self.mats['Borated Water'])
        self.u_gridsleeve.add_axial_section(self.s_grid2_top, self.u_grid_sleeve_i)
        self.u_gridsleeve.add_axial_section(self.s_grid3_bot, self.mats['Borated Water'])
        self.u_gridsleeve.add_axial_section(self.s_grid3_top, self.u_grid_sleeve_i)
        self.u_gridsleeve.add_axial_section(self.s_grid4_bot, self.mats['Borated Water'])
        self.u_gridsleeve.add_axial_section(self.s_grid4_top, self.u_grid_sleeve_i)
        self.u_gridsleeve.add_axial_section(self.s_grid5_bot, self.mats['Borated Water'])
        self.u_gridsleeve.add_axial_section(self.s_grid5_top, self.u_grid_sleeve_i)
        self.u_gridsleeve.add_axial_section(self.s_grid6_bot, self.mats['Borated Water'])
        self.u_gridsleeve.add_axial_section(self.s_grid6_top, self.u_grid_sleeve_i)
        self.u_gridsleeve.add_axial_section(self.s_grid7_bot, self.mats['Borated Water'])
        self.u_gridsleeve.add_axial_section(self.s_grid7_top, self.u_grid_sleeve_i)
        self.u_gridsleeve.add_axial_section(self.s_grid8_bot, self.mats['Borated Water'])
        self.u_gridsleeve.add_axial_section(self.s_grid8_top, self.u_grid_sleeve_tb)
        self.u_gridsleeve.add_axial_section(self.s_struct_upperNozzle_bot, self.mats['Borated Water'])
        self.u_gridsleeve.add_axial_section(self.s_struct_upperNozzle_top, self.mats['Water SPN'])
        self.u_gridsleeve.add_last_axial_section(self.mats['Borated Water'])
        self.u_gridsleeve.finalize()

    def _add_fuel_pincells(self):
        """ Adds BEAVRS fuel pincells """

        self.enrichments = ['1.6%', '2.4%', '3.1%', '3.2%', '3.4%']

        # Fuel radial surfaces

        self.s_fuel_pellet_OR = openmc.ZCylinder(name='Fuel pellet OR', r=c.pelletOR)
        self.s_fuel_clad_IR = openmc.ZCylinder(name='Fuel clad IR', r=c.cladIR)
        self.s_fuel_clad_OR = openmc.ZCylinder(name='Fuel clad OR', r=c.cladOR)
        self.s_fuel_plenumSpring_OR = openmc.ZCylinder(name='Fuel rod plenum spring OR', r=c.plenumSpringOR)

        # Fuel axial surfaces

        self.s_fuel_rod_bot = openmc.ZPlane(name='Fuel rod bottom', z0=c.fuel_Rod_bot)
        self.s_fuel_lowerFitting_bot = self.s_fuel_rod_bot
        self.s_fuel_lowerFitting_top = openmc.ZPlane(name='Fuel lower fitting top', z0=c.fuel_LowerFitting_top)
        self.s_fuel_activeFuel_bot = self.s_fuel_lowerFitting_top
        self.s_fuel_activeFuel_top = openmc.ZPlane(name='Fuel active region top', z0=c.fuel_ActiveFuel_top)
        self.s_fuel_plenum_bot = self.s_fuel_activeFuel_top
        self.s_fuel_plenum_top = openmc.ZPlane(name='Fuel plenum top', z0=c.fuel_Plenum_top)
        self.s_fuel_upperFitting_bot = self.s_fuel_plenum_top
        self.s_fuel_upperFitting_top = openmc.ZPlane(name='Fuel upper fitting top', z0=c.fuel_UpperFitting_top)

        # Fuel pincell universes

        self.u_fuel_active_pin = {}
        for enr in self.enrichments:
            self.u_fuel_active_pin[enr] = InfinitePinCell(name='Fuel rod active region - {0} enr'.format(enr))
            self.u_fuel_active_pin[enr].add_ring(self.mats['Fuel {0}'.format(enr)], self.s_fuel_pellet_OR)
            self.u_fuel_active_pin[enr].add_ring(self.mats['Helium'], self.s_fuel_clad_IR)
            self.u_fuel_active_pin[enr].add_last_ring(self.mats['Zircaloy 4'])
            self.u_fuel_active_pin[enr].finalize()

        self.u_fuel_plenum = InfinitePinCell(name='Fuel rod plenum')
        self.u_fuel_plenum.add_ring(self.mats['Inconel 718'], self.s_fuel_plenumSpring_OR)
        self.u_fuel_plenum.add_ring(self.mats['Helium'], self.s_fuel_clad_IR)
        self.u_fuel_plenum.add_last_ring(self.mats['Zircaloy 4'])
        self.u_fuel_plenum.finalize()

        # Fuel axial stack universes

        self.u_fuel_p = {}
        for enr in self.enrichments:
            self.u_fuel_p[enr] = AxialPinCell(name='Fuel rod - {0} enr'.format(enr))
            self.u_fuel_p[enr].add_axial_section(self.s_struct_supportPlate_bot, self.mats['Borated Water'])
            self.u_fuel_p[enr].add_axial_section(self.s_fuel_rod_bot, self.mats['SS304 SPN'])
            self.u_fuel_p[enr].add_axial_section(self.s_fuel_lowerFitting_top, self.mats['Zircaloy 4'])
            self.u_fuel_p[enr].add_axial_section(self.s_fuel_activeFuel_top, self.u_fuel_active_pin[enr])
            self.u_fuel_p[enr].add_axial_section(self.s_fuel_plenum_top, self.u_fuel_plenum)
            self.u_fuel_p[enr].add_axial_section(self.s_fuel_upperFitting_top, self.mats['Zircaloy 4'])
            self.u_fuel_p[enr].add_axial_section(self.s_struct_upperNozzle_bot, self.mats['Borated Water'])
            self.u_fuel_p[enr].add_axial_section(self.s_struct_upperNozzle_top, self.mats['SS304 SPN'])
            self.u_fuel_p[enr].add_last_axial_section(self.mats['Borated Water'])
            self.u_fuel_p[enr] = self.u_fuel_p[enr].add_wrapper(self.u_grids, self.s_fuel_clad_OR)
            self.u_fuel_p[enr].finalize()

    def _add_guide_tube_pincells(self):
        """ Adds BEAVRS guide tube pincells """

        # GT radial surfaces

        self.s_gt_IR = openmc.ZCylinder(name='Guide tube IR', r=c.guideTubeIR)
        self.s_gt_OR = openmc.ZCylinder(name='Guide tube OR', r=c.guideTubeOR)
        self.s_gt_dashpot_IR = openmc.ZCylinder(name='Guide tube IR below dashpot', r=c.guideTubeDashIR)
        self.s_gt_dashpot_OR = openmc.ZCylinder(name='Guide tube OR below dashpot', r=c.guideTubeDashOR)

        # GT axial surfaces

        self.s_gt_rod_bot = openmc.ZPlane(name='Bottom of GT rod', z0=c.gt_Rod_bot)
        self.s_gt_dashpot_bot = self.s_gt_rod_bot
        self.s_gt_dashpot_top = openmc.ZPlane(name='GT Dashpot plane', z0=c.gt_Dashpot_top)
        self.s_gt_rod_top = openmc.ZPlane(name='Top of GT rod', z0=c.gt_Rod_top)

        # GT pincell universes

        self.u_gt_dashpot = InfinitePinCell(name='Empty GT below the dashpot')
        self.u_gt_dashpot.add_ring(self.mats['Borated Water'], self.s_gt_dashpot_IR)
        self.u_gt_dashpot.add_ring(self.mats['Zircaloy 4'], self.s_gt_dashpot_OR)
        self.u_gt_dashpot.add_last_ring(self.mats['Borated Water'])
        self.u_gt_dashpot.finalize()

        self.u_gt_nodashpot_p = InfinitePinCell(name='Empty GT above the dashpot')
        self.u_gt_nodashpot_p.add_ring(self.mats['Borated Water'], self.s_gt_IR)
        self.u_gt_nodashpot_p.add_last_ring(self.mats['Zircaloy 4'])
        self.u_gt_nodashpot_p.finalize()

        # GT axial stack

        self.u_gt = AxialPinCell(name='Empty Guide Tube')
        self.u_gt.add_axial_section(self.s_struct_supportPlate_bot, self.mats['Borated Water'])
        self.u_gt.add_axial_section(self.s_gt_rod_bot, self.mats['Water SPN'])
        self.u_gt.add_axial_section(self.s_gt_dashpot_top, self.u_gt_dashpot)
        self.u_gt.add_axial_section(self.s_gt_rod_top, self.u_gt_nodashpot_p)
        self.u_gt.add_axial_section(self.s_struct_upperNozzle_top, self.mats['Water SPN'])
        self.u_gt.add_last_axial_section(self.mats['Borated Water'])
        self.u_gt = self.u_gt.add_wrapper(self.u_grids, self.s_gt_OR)
        self.u_gt.finalize()

        self.u_gt_nodashpot = AxialPinCell(name='Empty Guide Tube in Center Position')
        self.u_gt_nodashpot.add_axial_section(self.s_struct_supportPlate_bot, self.mats['Borated Water'])
        self.u_gt_nodashpot.add_axial_section(self.s_gt_rod_bot, self.mats['Water SPN'])
        self.u_gt_nodashpot.add_axial_section(self.s_gt_rod_top, self.u_gt_nodashpot_p)
        self.u_gt_nodashpot.add_axial_section(self.s_struct_upperNozzle_top, self.mats['Water SPN'])
        self.u_gt_nodashpot.add_last_axial_section(self.mats['Borated Water'])
        self.u_gt_nodashpot = self.u_gt_nodashpot.add_wrapper(self.u_grids, self.s_gt_OR)
        self.u_gt_nodashpot.finalize()

    def _add_instrument_tube_pincells(self):
        """ Adds BEAVRS instrument tube pincells to self object """

        # IT radial surfaces

        self.s_it_IR = openmc.ZCylinder(name='Instrument tube thimble IR', r=c.instrTubeIR)
        self.s_it_OR = openmc.ZCylinder(name='Instrument tube thimble OR', r=c.instrTubeOR)

        # IT pincell universe
        self.u_it_p = InfinitePinCell(name='Instrument tube thimble')
        self.u_it_p.add_ring(self.mats['Air'], self.s_it_IR)
        self.u_it_p.add_last_ring(self.mats['Zircaloy 4'])
        self.u_it_p.finalize()

        # IT pincell in support plane
        self.u_it_p_spn = InfinitePinCell(name='Instrument tube thimble support plane')
        self.u_it_p_spn.add_ring(self.mats['Air'], self.s_it_IR)
        self.u_it_p_spn.add_last_ring(self.mats['Zircaloy 4'])
        self.u_it_p_spn.finalize()

        # IT axial stack
        self.u_it = AxialPinCell(name='Instrument tube axial stack')
        self.u_it.add_axial_section(self.s_struct_supportPlate_bot, self.u_it_p)
        self.u_it.add_axial_section(self.s_fuel_rod_bot, self.u_it_p_spn)
        self.u_it.add_axial_section(self.s_struct_upperNozzle_bot, self.u_it_p)
        self.u_it.add_axial_section(self.s_struct_upperNozzle_top, self.mats['Water SPN'])
        self.u_it.add_last_axial_section(self.mats['Borated Water'])
        self.u_it = self.u_it.add_wrapper(self.u_gt_nodashpot, self.s_it_OR)
        self.u_it.finalize()

        # IT axial stack - empty
        self.u_it_nt = self.u_gt_nodashpot

    def _add_bpra_pincells(self):
        """ Adds BEAVRS BPRA pincells """

        # BP radial surfaces

        self.s_bp_innerclad_IR = openmc.ZCylinder(name='BPRA rod radius 1', r=c.burnabs1)
        self.s_bp_innerclad_OR = openmc.ZCylinder(name='BPRA rod radius 2', r=c.burnabs2)
        self.s_bp_poison_IR = openmc.ZCylinder(name='BPRA rod radius 3', r=c.burnabs3)
        self.s_bp_poison_OR = openmc.ZCylinder(name='BPRA rod radius 4', r=c.burnabs4)
        self.s_bp_outerclad_IR = openmc.ZCylinder(name='BPRA rod radius 5', r=c.burnabs5)
        self.s_bp_outerclad_OR = openmc.ZCylinder(name='BPRA rod radius 6', r=c.burnabs6)

        # BP axial surfaces

        self.s_bp_rod_bot = openmc.ZPlane(name='Bottom of BPRA rod', z0=c.bpra_Rod_bot)
        self.s_bp_lowerFitting_bot = self.s_bp_rod_bot
        self.s_bp_lowerFitting_top = openmc.ZPlane(name='Top of lower fitting in BPRA rod', z0=c.bpra_LowerFitting_top)
        self.s_bp_active_bot = self.s_bp_lowerFitting_top
        self.s_bp_active_top = openmc.ZPlane(name='Top of active poison in BPRA rod', z0=c.bpra_Active_top)
        self.s_bp_plenum_bot = self.s_bp_active_top
        self.s_bp_plenum_top = openmc.ZPlane(name='Top of plenum in BPRA rod', z0=c.bpra_Plenum_top)
        self.s_bp_rod_top = openmc.ZPlane(name='Top of BPRA rod', z0=c.bpra_Rod_top)

        # BP pincell universes

        self.u_bp_activePoison = InfinitePinCell(name='BPRA rod active poison')
        self.u_bp_activePoison.add_ring(self.mats['Air'], self.s_bp_innerclad_IR)
        self.u_bp_activePoison.add_ring(self.mats['SS304'], self.s_bp_innerclad_OR)
        self.u_bp_activePoison.add_ring(self.mats['Helium'], self.s_bp_poison_IR)
        self.u_bp_activePoison.add_ring(self.mats['Borosilicate Glass'], self.s_bp_poison_OR)
        self.u_bp_activePoison.add_ring(self.mats['Helium'], self.s_bp_outerclad_IR)
        self.u_bp_activePoison.add_last_ring(self.mats['SS304'])
        self.u_bp_activePoison.finalize()

        self.u_bp_plenum = InfinitePinCell(name='BPRA rod plenum')
        self.u_bp_plenum.add_ring(self.mats['Air'], self.s_bp_innerclad_IR)
        self.u_bp_plenum.add_ring(self.mats['SS304'], self.s_bp_innerclad_OR)
        self.u_bp_plenum.add_ring(self.mats['Helium'], self.s_bp_outerclad_IR)
        self.u_bp_plenum.add_last_ring(self.mats['SS304'])
        self.u_bp_plenum.finalize()

        # BP axial stack universe

        self.u_bp = AxialPinCell(name='BPRA rod')
        self.u_bp.add_axial_section(self.s_struct_supportPlate_bot, self.mats['Borated Water'])
        self.u_bp.add_axial_section(self.s_struct_lowerNozzle_top, self.mats['Water SPN'])
        self.u_bp.add_axial_section(self.s_bp_rod_bot, self.mats['Borated Water'])
        self.u_bp.add_axial_section(self.s_bp_lowerFitting_top, self.mats['SS304'])
        self.u_bp.add_axial_section(self.s_bp_active_top, self.u_bp_activePoison)
        self.u_bp.add_axial_section(self.s_bp_plenum_top, self.u_bp_plenum)
        self.u_bp.add_axial_section(self.s_bp_rod_top, self.mats['SS304'])
        self.u_bp.add_last_axial_section(self.mats['Borated Water'])
        self.u_bp = self.u_bp.add_wrapper(self.u_gt, self.s_bp_outerclad_OR)
        self.u_bp.finalize()

    def _add_rcca_pincells(self):
        """ Adds BEAVRS RCCA pincells """

        # RCCA rod radial surfaces

        self.s_rcca_clad_IR = openmc.ZCylinder(name='RCCA rod clad IR', r=c.rcca_clad_IR)
        self.s_rcca_clad_OR = openmc.ZCylinder(name='RCCA rod clad OR', r=c.rcca_clad_OR)
        self.s_rcca_b4c_OR = openmc.ZCylinder(name='RCCA rod B4C OR', r=c.rcca_b4c_OR)
        self.s_rcca_aic_OR = openmc.ZCylinder(name='RCCA rod AIC OR', r=c.rcca_aic_OR)
        self.s_rcca_spacer_OR = openmc.ZCylinder(name='RCCA rod spacer OR', r=c.rcca_spacer_OR)
        self.s_rcca_spring_OR = openmc.ZCylinder(name='RCCA rod plenum spring OR', r=c.rcca_spring_OR)

        # RCCA rod axial surfaces

        self.s_rcca_rod_bot = {}
        self.s_rcca_lowerFitting_top = {}
        self.s_rcca_aic_top = {}
        self.s_rcca_b4c_top = {}
        self.s_rcca_spacer_top = {}
        self.s_rcca_plenum_top = {}
        for b in sorted(c.rcca_banks):
            d = c.rcca_bank_steps_withdrawn[b]*c.rcca_StepWidth
            self.s_rcca_rod_bot[b] = openmc.ZPlane(name='Bottom of RCCA rod bank {0}'.format(b), z0=c.rcca_Rod_bot + d)
            self.s_rcca_lowerFitting_top[b] = openmc.ZPlane(name='Top of RCCA rod lower fitting bank {0}'.format(b), z0=c.rcca_LowerFitting_top + d)
            self.s_rcca_aic_top[b] = openmc.ZPlane(name='Top of RCCA rod AIC bank {0}'.format(b), z0=c.rcca_AIC_top + d)
            self.s_rcca_b4c_top[b] = openmc.ZPlane(name='Top of RCCA rod B4C bank {0}'.format(b), z0=c.rcca_B4C_top + d)
            self.s_rcca_spacer_top[b] = openmc.ZPlane(name='Top of RCCA rod spacer bank {0}'.format(b), z0=c.rcca_Spacer_top + d)
            self.s_rcca_plenum_top[b] = openmc.ZPlane(name='Top of RCCA rod plenum bank {0}'.format(b), z0=c.rcca_Plenum_top + d)

        # RCCA pincell universes

        self.u_rcca_plenum = InfinitePinCell(name='RCCA plenum')
        self.u_rcca_plenum.add_ring(self.mats['Inconel 718'], self.s_rcca_spring_OR)
        self.u_rcca_plenum.add_ring(self.mats['Helium'], self.s_rcca_clad_IR)
        self.u_rcca_plenum.add_last_ring(self.mats['SS304'])
        self.u_rcca_plenum.finalize()

        self.u_rcca_aic = InfinitePinCell(name='RCCA AIC')
        self.u_rcca_aic.add_ring(self.mats['Ag-In-Cd'], self.s_rcca_aic_OR)
        self.u_rcca_aic.add_ring(self.mats['Helium'], self.s_rcca_clad_IR)
        self.u_rcca_aic.add_last_ring( self.mats['SS304'])
        self.u_rcca_aic.finalize()

        self.u_rcca_b4c = InfinitePinCell(name='RCCA B4C')
        self.u_rcca_b4c.add_ring(self.mats['B4C'], self.s_rcca_b4c_OR)
        self.u_rcca_b4c.add_ring(self.mats['Helium'], self.s_rcca_clad_IR)
        self.u_rcca_b4c.add_last_ring(self.mats['SS304'])
        self.u_rcca_b4c.finalize()

        self.u_rcca_spacer = InfinitePinCell(name='RCCA Spacer')
        self.u_rcca_spacer.add_ring(self.mats['SS304'], self.s_rcca_spacer_OR)
        self.u_rcca_spacer.add_ring(self.mats['Helium'], self.s_rcca_clad_IR)
        self.u_rcca_spacer.add_last_ring(self.mats['SS304'])
        self.u_rcca_spacer.finalize()

        # RCCA rod axial stack

        self.u_rcca = {}
        for b in sorted(c.rcca_banks):
            self.u_rcca[b] = AxialPinCell(name='RCCA bank {0}'.format(b))
            self.u_rcca[b].add_axial_section(self.s_struct_supportPlate_bot, self.mats['Borated Water'])
            self.u_rcca[b].add_axial_section(self.s_struct_lowerNozzle_top, self.mats['Water SPN'])
            self.u_rcca[b].add_axial_section(self.s_rcca_rod_bot[b], self.mats['Borated Water'])
            self.u_rcca[b].add_axial_section(self.s_rcca_lowerFitting_top[b], self.mats['SS304'])
            self.u_rcca[b].add_axial_section(self.s_rcca_aic_top[b], self.u_rcca_aic)
            self.u_rcca[b].add_axial_section(self.s_rcca_b4c_top[b], self.u_rcca_b4c)
            self.u_rcca[b].add_axial_section(self.s_rcca_spacer_top[b], self.u_rcca_spacer)
            self.u_rcca[b].add_axial_section(self.s_rcca_plenum_top[b], self.u_rcca_plenum)
            self.u_rcca[b].add_last_axial_section(self.mats['SS304'])
            self.u_rcca[b] = self.u_rcca[b].add_wrapper(self.u_gt, self.s_rcca_clad_OR)
            self.u_rcca[b].finalize()
