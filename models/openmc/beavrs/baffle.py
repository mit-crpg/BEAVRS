"""baffle.py

Provides a container class for BEAVRS baffle universes

These are assemblies that go in the main core lattice around the edges of the
assemblies

"""

import openmc

import beavrs.constants as c
from beavrs.corebuilder import InfinitePinCell


class Baffle(object):

    def __init__(self, assemblies, mats):
        """ Creates BEAVRS baffle universes """

        self.assem = assemblies
        self.mats = mats

        self._add_baffle_universes()

    def _add_baffle_universes(self):
        """ Adds BEAVRS baffle universes """

        self.dummy = openmc.ZCylinder(name="Dummy filling universe", r=4000.)

        # North Baffle
        self.u_baffle_N = openmc.Universe(name='Baffle North')
        self.s_baffle_N_gap = openmc.YPlane(name='North Baffle Water Gap Surface',
                                            y0=c.latticePitch/2-c.baffleWaterGap)
        self.s_baffle_N = openmc.YPlane(name='North Baffle Surface',
                                        y0=c.latticePitch/2 - c.baffleWaterGap
                                        - c.baffleWidth)
        self.c_baffle_N1 = openmc.Cell(name='North Baffle Water Gap',
                                       fill=self.mats['Borated Water'])
        self.c_baffle_N1.region = +self.s_baffle_N_gap
        self.c_baffle_N2 = openmc.Cell(name='North Baffle Steel',
                                       fill=self.mats['SS304'])
        self.c_baffle_N2.region = -self.s_baffle_N_gap & +self.s_baffle_N
        self.c_baffle_N3 = openmc.Cell(name='North Baffle Outer Water',
                                       fill=self.mats['Borated Water'])
        self.c_baffle_N3.region = -self.s_baffle_N
        self.u_baffle_N.add_cells(
          [self.c_baffle_N1,self.c_baffle_N2,self.c_baffle_N3])

        # West Baffle
        self.u_baffle_W = InfinitePinCell(name="Baffle West")
        self.u_baffle_W.add_ring(self.u_baffle_N, self.dummy, rot=[0, 0, 90])
        self.u_baffle_W.add_last_ring(self.mats['Borated Water'])
        self.u_baffle_W.finalize()

        # South Baffle
        self.u_baffle_S = InfinitePinCell(name="Baffle South")
        self.u_baffle_S.add_ring(self.u_baffle_N, self.dummy, rot=[0, 0, 180])
        self.u_baffle_S.add_last_ring(self.mats['Borated Water'])
        self.u_baffle_S.finalize()

        # East Baffle
        self.u_baffle_E = InfinitePinCell(name="Baffle East")
        self.u_baffle_E.add_ring(self.u_baffle_N, self.dummy, rot=[0, 0, 270])
        self.u_baffle_E.add_last_ring(self.mats['Borated Water'])
        self.u_baffle_E.finalize()

        # North West Corner Baffle
        self.u_baffle_NW = openmc.Universe(name='Baffle North West Corner')
        self.s_baffle_W_gap = openmc.XPlane(name='West Baffle Water Gap Surface',
                                            x0=c.baffleWaterGap-c.latticePitch/2)
        self.s_baffle_W = openmc.XPlane(name='West Baffle Surface',
                                        x0=c.baffleWaterGap + c.baffleWidth
                                        - c.latticePitch/2)
        self.c_baffle_C1 = openmc.Cell(name='Corner Baffle Water Gap N',
                                       fill=self.mats['Borated Water'])
        self.c_baffle_C1.region = +self.s_baffle_N_gap
        self.c_baffle_C2 = openmc.Cell(name='Corner Baffle Water Gap W',
                                       fill=self.mats['Borated Water'])
        self.c_baffle_C2.region = -self.s_baffle_N_gap & -self.s_baffle_W_gap
        self.c_baffle_C3 = openmc.Cell(name='Corner Baffle Steel N',
                                       fill=self.mats['SS304'])
        self.c_baffle_C3.region = \
          -self.s_baffle_N_gap & +self.s_baffle_N & +self.s_baffle_W_gap
        self.c_baffle_C4 = openmc.Cell(name='Corner Baffle Steel W',
                                       fill=self.mats['SS304'])
        self.c_baffle_C4.region = \
          -self.s_baffle_N & +self.s_baffle_W_gap & -self.s_baffle_W
        self.c_baffle_C5 = openmc.Cell(name='Corner Baffle Outer Water',
                                       fill=self.mats['Borated Water'])
        self.c_baffle_C5.region = -self.s_baffle_N & +self.s_baffle_W
        self.u_baffle_NW.add_cells([self.c_baffle_C1, self.c_baffle_C2,
                                    self.c_baffle_C3, self.c_baffle_C4,
                                    self.c_baffle_C5])

        # South West Corner Baffle
        self.u_baffle_SW = InfinitePinCell(name="Baffle South West Corner")
        self.u_baffle_SW.add_ring(self.u_baffle_NW, self.dummy, rot=[0, 0, 90])
        self.u_baffle_SW.add_last_ring(self.mats['Borated Water'])
        self.u_baffle_SW.finalize()

        # South East Corner Baffle
        self.u_baffle_SE = InfinitePinCell(name="Baffle South East Corner")
        self.u_baffle_SE.add_ring(self.u_baffle_NW, self.dummy, rot=[0, 0, 180])
        self.u_baffle_SE.add_last_ring(self.mats['Borated Water'])
        self.u_baffle_SE.finalize()

        # North East Corner Baffle
        self.u_baffle_NE = InfinitePinCell(name="Baffle North East Corner")
        self.u_baffle_NE.add_ring(self.u_baffle_NW, self.dummy, rot=[0, 0, 270])
        self.u_baffle_NE.add_last_ring(self.mats['Borated Water'])
        self.u_baffle_NE.finalize()

        # North West Tip Baffle
        self.u_baffle_NWT = openmc.Universe(name='Baffle North West Tip')
        self.c_baffle_C1 = openmc.Cell(name='Tip Baffle Water Gap',
                                       fill=self.mats['Borated Water'])
        self.c_baffle_C1.region = +self.s_baffle_N_gap & -self.s_baffle_W_gap
        self.c_baffle_C2 = openmc.Cell(name='Tip Baffle steel N',
                                       fill=self.mats['SS304'])
        self.c_baffle_C2.region = \
          +self.s_baffle_N & -self.s_baffle_W & +self.s_baffle_W_gap
        self.c_baffle_C3 = openmc.Cell(name='Tip Baffle Steel W',
                                       fill=self.mats['SS304'])
        self.c_baffle_C3.region = \
          -self.s_baffle_N_gap & +self.s_baffle_N & -self.s_baffle_W_gap
        self.c_baffle_C4 = openmc.Cell(name='Tip Baffle Outer Water N',
                                       fill=self.mats['Borated Water'])
        self.c_baffle_C4.region = +self.s_baffle_N & +self.s_baffle_W
        self.c_baffle_C5 = openmc.Cell(name='Tip Baffle Outer Water W',
                                       fill=self.mats['Borated Water'])
        self.c_baffle_C5.region = -self.s_baffle_N & -self.s_baffle_W
        self.c_baffle_C6 = openmc.Cell(name='Tip Baffle Outer Water SE',
                                       fill=self.mats['Borated Water'])
        self.c_baffle_C6.region = -self.s_baffle_N & +self.s_baffle_W
        self.u_baffle_NWT.add_cells([self.c_baffle_C1, self.c_baffle_C2,
                                     self.c_baffle_C3, self.c_baffle_C4,
                                     self.c_baffle_C5, self.c_baffle_C6])

        # South West Tip Baffle
        self.u_baffle_SWT = InfinitePinCell(name="Baffle South West Tip")
        self.u_baffle_SWT.add_ring(self.u_baffle_NWT, self.dummy, rot=[0, 0, 90])
        self.u_baffle_SWT.add_last_ring(self.mats['Borated Water'])
        self.u_baffle_SWT.finalize()

        # South East Tip Baffle
        self.u_baffle_SET = InfinitePinCell(name="Baffle South East Tip")
        self.u_baffle_SET.add_ring(self.u_baffle_NWT, self.dummy, rot=[0, 0, 180])
        self.u_baffle_SET.add_last_ring(self.mats['Borated Water'])
        self.u_baffle_SET.finalize()

        # North East Tip Baffle
        self.u_baffle_NET = InfinitePinCell(name="Baffle North East Tip")
        self.u_baffle_NET.add_ring(self.u_baffle_NWT, self.dummy, rot=[0, 0, 270])
        self.u_baffle_NET.add_last_ring(self.mats['Borated Water'])
        self.u_baffle_NET.finalize()

        self.universes = {}
        self.universes['bafn_'] = self.u_baffle_S
        self.universes['bafs_'] = self.u_baffle_N
        self.universes['bafe_'] = self.u_baffle_W
        self.universes['bafw_'] = self.u_baffle_E
        self.universes['bafnw'] = self.u_baffle_SET
        self.universes['bafne'] = self.u_baffle_SWT
        self.universes['bafsw'] = self.u_baffle_NET
        self.universes['bafse'] = self.u_baffle_NWT
        self.universes['bfcnw'] = self.u_baffle_SE
        self.universes['bfcne'] = self.u_baffle_SW
        self.universes['bfcsw'] = self.u_baffle_NE
        self.universes['bfcse'] = self.u_baffle_NW
