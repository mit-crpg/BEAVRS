#!/usr/bin/env python

# Packages
import os
from copy import copy
from collections import OrderedDict

import numpy as np

import openmc
from openmc.data import atomic_mass, atomic_weight
import beavrs.constants as c


MB10 = atomic_mass('B10')
MB11 = atomic_mass('B11')
MU234 = atomic_mass('U234')
MU235 = atomic_mass('U235')
MU238 = atomic_mass('U238')


def openmc_materials(ppm):

    # Initialize openmc material dictionary
    mats = OrderedDict()

##############################################
# Create materials that use natural abundances
##############################################

    # Create air material
    mats['Air'] = openmc.Material(name='Air')
    mats['Air'].temperature = 300
    mats['Air'].set_density('g/cc', 0.000616)
    mats['Air'].add_element('O', 0.2095, 'ao')
    mats['Air'].add_element('N', 0.7809, 'ao')
    mats['Air'].add_element('Ar', 0.00933, 'ao')
    mats['Air'].add_element('C', 0.00027, 'ao')

    # Create stainless steel material
    mats['SS304'] = openmc.Material(name='SS304')
    mats['SS304'].temperature = 300
    mats['SS304'].set_density('g/cc', 8.03)
    mats['SS304'].add_element('Si', 0.0060, 'wo')
    mats['SS304'].add_element('Cr', 0.1900, 'wo')
    mats['SS304'].add_element('Mn', 0.0200, 'wo')
    mats['SS304'].add_element('Fe', 0.6840, 'wo')
    mats['SS304'].add_element('Ni', 0.1000, 'wo')

    # Create Ag-In-Cd control rod material
    mats['Ag-In-Cd'] = openmc.Material(name='Ag-In-Cd')
    mats['Ag-In-Cd'].temperature = 300
    mats['Ag-In-Cd'].set_density('g/cc', 10.16)
    mats['Ag-In-Cd'].add_element('Ag', 0.80, 'wo')
    mats['Ag-In-Cd'].add_element('In', 0.15, 'wo')
    mats['Ag-In-Cd'].add_element('Cd', 0.05, 'wo')

    # Create B4C control rod material
    mats['B4C'] = openmc.Material(name='B4C')
    mats['B4C'].temperature = 300
    mats['B4C'].set_density('g/cc', 1.76)
    mats['B4C'].add_element('B', 0.7826, 'wo')
    mats['B4C'].add_element('C', 0.2174, 'wo')

    # Create He gas gap material
    mats['Helium'] = openmc.Material(name='Helium')
    mats['Helium'].temperature = 300
    mats['Helium'].set_density('g/cc', 0.0015981)
    mats['Helium'].add_element('He', 1.0, 'wo')

    # Create inconel 718 material
    mats['Inconel 718'] = openmc.Material(name='Inconel 718')
    mats['Inconel 718'].temperature = 300
    mats['Inconel 718'].set_density('g/cc', 8.2)
    mats['Inconel 718'].add_element('Si', 0.0035, 'wo')
    mats['Inconel 718'].add_element('Cr', 0.1896, 'wo')
    mats['Inconel 718'].add_element('Mn', 0.0087, 'wo')
    mats['Inconel 718'].add_element('Fe', 0.2863, 'wo')
    mats['Inconel 718'].add_element('Ni', 0.5119, 'wo')

    # Create zircaloy 4 material
    mats['Zircaloy 4'] = openmc.Material(name='Zircaloy 4')
    mats['Zircaloy 4'].temperature = 300
    mats['Zircaloy 4'].set_density('g/cc', 6.55)
    mats['Zircaloy 4'].add_element('O', 0.00125, 'wo')
    mats['Zircaloy 4'].add_element('Cr', 0.0010, 'wo')
    mats['Zircaloy 4'].add_element('Fe', 0.0021, 'wo')
    mats['Zircaloy 4'].add_element('Zr', 0.98115, 'wo')
    mats['Zircaloy 4'].add_element('Sn', 0.0145, 'wo')

    # Create carbon steel material
    mats['Carbon Steel'] = openmc.Material(name='Carbon Steel')
    mats['Carbon Steel'].temperature = 300
    mats['Carbon Steel'].set_density('g/cc', 7.8)
    mats['Carbon Steel'].add_element('C', 0.00270, 'wo')
    mats['Carbon Steel'].add_element('Mn', 0.00750, 'wo')
    mats['Carbon Steel'].add_element('P', 0.00025, 'wo')
    mats['Carbon Steel'].add_element('S', 0.00025, 'wo')
    mats['Carbon Steel'].add_element('Si', 0.00400, 'wo')
    mats['Carbon Steel'].add_element('Ni', 0.00750, 'wo')
    mats['Carbon Steel'].add_element('Cr', 0.00350, 'wo')
    mats['Carbon Steel'].add_element('Mo', 0.00625, 'wo')
    mats['Carbon Steel'].add_element('V', 0.00050, 'wo')
    mats['Carbon Steel'].add_element('Nb', 0.00010, 'wo')
    mats['Carbon Steel'].add_element('Cu', 0.00200, 'wo')
    mats['Carbon Steel'].add_element('Ca', 0.00015, 'wo')
    mats['Carbon Steel'].add_element('B', 0.00003, 'wo')
    mats['Carbon Steel'].add_element('Ti', 0.00015, 'wo')
    mats['Carbon Steel'].add_element('Al', 0.00025, 'wo')
    mats['Carbon Steel'].add_element('Fe', 0.96487, 'wo')

##############################################
# Create special materials
##############################################

########## Enriched UO2 Fuel #################

    # Specify enrichments to be calculated
    enrs = [0.0161006, 0.0239993, 0.0310221, 0.0319547, 0.0340585]
    dens = [10.31341, 10.29748, 10.30166, 10.34115, 10.35917]

    # Loop around enrichments
    for enr, den in zip(enrs, dens):

        # Calculate molar mass of Uranium
        enr_25 = enr
        enr_24 = 0.008*enr_25
        enr_28 = 1.0 - (enr_24 + enr_25)
        MU = 1.0/(enr_24/MU234 + enr_25/MU235 + enr_28/MU238)

        # Determine molar mass of UO2
        MUO2 = MU + 2.0*atomic_weight('O')

        # Compute weight percent of U in UO2
        wUpUO2 = MU/MUO2

        # Calculate Uranium atom fraction
        a_U = wUpUO2*MUO2/MU

        # Calculate Oxygen atom fraction
        a_O = (1.0 - wUpUO2)*MUO2/atomic_weight('O')

        # Create material
        name = enr*100
        mat_name = 'Fuel {0:1.1f}%'.format(name)
        mats[mat_name] = openmc.Material(name=mat_name)
        mats[mat_name].temperature = 300
        mats[mat_name].set_density('g/cc', den)
        mats[mat_name].add_element('O', a_O, 'ao')
        mats[mat_name].add_element('U', a_U, 'ao', enrichment=enr*100)

########## Borosilicate Glass #################

    # CASMO weight fractions
    wO_bsg = 0.5481
    wAl_bsg = 0.0344
    wSi_bsg = 0.3787
    wB10_bsg = 0.0071
    wB11_bsg = 0.0317

    # Molar mass of BSG
    M_bsg = 1.0/(wO_bsg/atomic_weight('O') + wAl_bsg/atomic_weight('Al') + \
                 wSi_bsg/atomic_weight('Si') + wB10_bsg/MB10 + wB11_bsg/MB11)

    # Compute atom fractions
    aO_bsg = wO_bsg*M_bsg/atomic_weight('O')
    aAl_bsg = wAl_bsg*M_bsg/atomic_weight('Al')
    aSi_bsg = wSi_bsg*M_bsg/atomic_weight('Si')
    aB10_bsg = wB10_bsg*M_bsg/MB10
    aB11_bsg = wB11_bsg*M_bsg/MB11

    # Create material
    mats['Borosilicate Glass'] = openmc.Material(name='Borosilicate Glass')
    mats['Borosilicate Glass'].temperature = 300
    mats['Borosilicate Glass'].set_density('g/cc', 2.26)
    mats['Borosilicate Glass'].add_element('O', aO_bsg, 'ao')
    mats['Borosilicate Glass'].add_element('Si', aSi_bsg, 'ao')
    mats['Borosilicate Glass'].add_element('Al', aAl_bsg, 'ao')
    mats['Borosilicate Glass'].add_nuclide('B10', aB10_bsg, 'ao')
    mats['Borosilicate Glass'].add_nuclide('B11', aB11_bsg, 'ao')

########## Borated Water #################

    # Density of clean water at 2250 psia T=560F NIST
    h2o_dens = 0.73986

    # Compute weight percent of natural boron in borated water
    wB_Bh2o = ppm*1.0e-6

    # Borated water density
    rho_Bh2o = h2o_dens/(1 - wB_Bh2o)

    # Compute weight percent of clean water in borated water
    wh2o_Bh2o = 1.0 - wB_Bh2o

    # Compute molecular mass of clean water
    M_h2o = 2*atomic_weight('H') + atomic_weight('O')

    # Compute molecular mass of borated water
    M_Bh2o = 1.0/(wB_Bh2o/atomic_weight('B') + wh2o_Bh2o/M_h2o)

    # Compute atom fractions of boron and water
    aB_Bh2o = wB_Bh2o*M_Bh2o/atomic_weight('B')
    ah2o_Bh2o = wh2o_Bh2o*M_Bh2o/M_h2o

    # Compute atom fractions of hydrogen
    ah_Bh2o = 2.0*ah2o_Bh2o
    aho_Bh2o = ah2o_Bh2o

    # Create material
    mats['Borated Water'] = openmc.Material(name='Borated Water')
    mats['Borated Water'].temperature = 300
    mats['Borated Water'].set_density('g/cc', rho_Bh2o)
    mats['Borated Water'].add_element('B', aB_Bh2o, 'ao')
    mats['Borated Water'].add_element('H', ah_Bh2o, 'ao')
    mats['Borated Water'].add_element('O', aho_Bh2o, 'ao')
    mats['Borated Water'].add_s_alpha_beta(name='c_H_in_H2O')

########## Nozzle / Support Plate Borated Materials #################

    # Calculate volume of water and steel in Nozzle / Support Plate for a
    # single assembly
    Bh2o_spn_vol = c.latticePitch**2 - float(c.n_nozzle_pins)*np.pi*c.cladOR**2
    ss_spn_vol = float(c.n_nozzle_pins)*np.pi*c.cladOR**2

    # From ML033530020 volw/volss
    Bh2o_vol_frac = c.nozzle_water_vol_frac
    ss_vol_frac = c.nozzle_ss_vol_frac
    Bh2o_spn_actualvol = (c.latticePitch**2)*Bh2o_vol_frac
    ss_spn_actualvol = (c.latticePitch**2)*ss_vol_frac

    # adjust density such that mass of water and steel are conserved
    rho_Bh2o_spn = (rho_Bh2o * Bh2o_spn_actualvol) / Bh2o_spn_vol
    rho_ss_spn = (8.03 * ss_spn_actualvol) / ss_spn_vol

    # Create borated water
    mats['Water SPN'] = openmc.Material(name='Water SPN')
    mats['Water SPN'].set_density('g/cc', rho_Bh2o_spn)
    mats['Water SPN'].add_element('B', aB_Bh2o, 'ao')
    mats['Water SPN'].add_element('H', ah_Bh2o, 'ao')
    mats['Water SPN'].add_element('O', aho_Bh2o, 'ao')
    mats['Water SPN'].add_s_alpha_beta(name='c_H_in_H2O')

    # Create stainless steel
    mats['SS304 SPN'] = openmc.Material(name='SS SPN')
    mats['SS304 SPN'].temperature = 300
    mats['SS304 SPN'].set_density('g/cc', rho_ss_spn)
    mats['SS304 SPN'].add_element('Si', 0.0060, 'wo')
    mats['SS304 SPN'].add_element('Cr', 0.1900, 'wo')
    mats['SS304 SPN'].add_element('Mn', 0.0200, 'wo')
    mats['SS304 SPN'].add_element('Fe', 0.6840, 'wo')
    mats['SS304 SPN'].add_element('Ni', 0.1000, 'wo')

    return mats
