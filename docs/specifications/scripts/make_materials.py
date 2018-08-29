#!/usr/bin/env python

import sys
import os

from beavrs.materials import openmc_materials
from openmc.data import NATURAL_ABUNDANCE, atomic_weight

# LaTeX template
latex = """\\begin{{matitem}}{{{title}}}{{{label}}}{{num:{numlabel}_mat}}
  \\centering
  \\begin{{tabular}}{{l c}}
    \\toprule
    Density (g/cc) & {density:.9g} \\\\
    \\midrule
    Isotope & Atom Density (atom/b-cm) \\\\
    \\midrule
    \\midrule
{isotopes}
    \\bottomrule
  \\end{{tabular}}
\\end{{matitem}}
"""

latex_2col = """\\begin{{matitem}}{{{title}}}{{{label}}}{{num:{numlabel}_mat}}
  \\centering
  \\begin{{tabular}}{{l c l c}}
    \\toprule
    Density (g/cc) & {density:.9g} \\\\
    \\midrule
    Isotope & Atom Density (atom/b-cm) & Isotope & Atom Density (atom/b-cm) \\\\
    \\midrule
    \\midrule
{isotopes}
    \\bottomrule
  \\end{{tabular}}
\\end{{matitem}}
"""

latex_ele_mass = """  \\begin{{longtable}}{{l c l c}}
    \\toprule
    Element & Mass [amu] & Element & Mass [amu] \\\\
    \\midrule
    \\midrule
{elements}
    \\bottomrule
  \\end{{longtable}}"""

latex_nuc_abund = """  \\begin{{longtable}}{{l c l c}}
    \\toprule
    Isotope & Fractional Abundance & Isotope & Fractional Abundance \\\\
    \\midrule
    \\midrule
{isotopes}
    \\bottomrule
  \\end{{longtable}}"""


# converting material name to latex latex file name
mat_table_filename = {
    "Air": "air",
    "SS304": "SS304",
    "Ag-In-Cd": "aic_rod",
    "B4C": "b4c_rod",
    "Helium": "helium",
    "Inconel 718": "inconel",
    "Zircaloy 4": "zirc",
    "Carbon Steel": "carbonsteel",
    "Fuel 1.6%": "fuel16",
    "Fuel 2.4%": "fuel24",
    "Fuel 3.1%": "fuel31",
    "Fuel 3.2%": "fuel32",
    "Fuel 3.4%": "fuel34",
    "Borosilicate Glass": "borosilicate",
    "Borated Water": "water",
    "Water SPN": "water_spn",
    "SS SPN": "ss_spn"
}

# converting material name to title of material in latex table
mat_table_titles = {
    "SS304": "Stainless Steel 304",
    "Ag-In-Cd": "Ag-In-Cd Control Rods",
    "B4C": "B4C Control Rods",
    "Fuel 1.6%": "Fuel 1.6\\% Enriched",
    "Fuel 2.4%": "Fuel 2.4\\% Enriched",
    "Fuel 3.1%": "Fuel 3.1\\% Enriched",
    "Fuel 3.2%": "Fuel 3.2\\% Enriched",
    "Fuel 3.4%": "Fuel 3.4\\% Enriched",
    "Water SPN": "Nozzle / Support Plate Borated Water",
    "SS SPN": "Nozzle / Support Plate Stainless Steel"
}

def write_materials(base):
    """ setup all beavrs materials and write them out to latex tables """

    # setup all beavrs materials
    mats = openmc_materials(ppm=975)

    # set of all appeared elements and isotopes
    used_elements_set = set() 
    used_isotopes_set = set() 

    # Write out material tables
    os.chdir(base)
    os.chdir('specifications/materials/tables')
    for key, mat in mats.items():
        # latex table file name
        if mat.name in mat_table_filename:
            name = mat_table_filename[mat.name]
        else:
            name = mat.name
            name = name.replace(' ','')
            name = name.replace('.','')
            name = name.replace('%','')

        # material title 
        if mat.name in mat_table_titles:
            title = mat_table_titles[mat.name]
        else:
            title = mat.name

        # Set some output parameters
        latex_dict = {
        'density':mat.density,
        'label':"mat_{0}".format(name),
        'numlabel':name,
        'title':title
        }

        # Get all nuclides atom density
        nuclides = mat.get_nuclide_atom_densities()

        # Create isotope string
        iso_str = ''
        if mat.name == 'Carbon Steel': # this one we want two columns
            i = 0
            for key, (iso, den) in sorted(nuclides.items()):
                if i%2 == 0:
                    nuc1 = iso.name
                    den1 = nuclides[iso][1]
                else:
                    iso_str += "{0} & {1:6.4e} & {2} & {3:6.4e}\\\\\n".format(
                                    nuc1, den1, iso.name, nuclides[iso][1])
                i += 1

            if i%2 == 1:
                iso_str += "{0} & {1:6.4e} & {2} & {3}\\\\\n".format(
                                iso.name, nuclides[iso][1], "", "")
            latex_dict.update({'isotopes':iso_str})
        else:
            for key, (iso, den) in sorted(nuclides.items()):
                iso_str += "{0} & {1:6.4e} \\\\\n".format(iso.name, den)
            latex_dict.update({'isotopes':iso_str})

        # Write latex file
        with open('{0}_table.tex'.format(name), 'w') as fh:
            if mat.name == 'Carbon Steel':
                fh.write(latex_2col.format(**latex_dict))
            else:
                fh.write(latex.format(**latex_dict))

        # Update elements and isotopes set
        for ele in mat.elements:
            used_elements_set.add(ele[0].name)
        for iso in mat.get_nuclides():
            used_isotopes_set.add(iso)

    os.chdir(base)

    # Write out isotope masses and abundances
    os.chdir('backmatter')
    with open('element_masses.tex', 'w') as fh:
        ele_str = ""
        flip = False
        for ele in sorted(used_elements_set):
            ele_str += "{0} & {1:.6f} ".format(ele, atomic_weight(ele))
            if not flip:
                ele_str += "& "
                flip = True
            else:
                ele_str += "\\\\\n"
                flip = False
        if flip:
            ele_str += "& \\\\\n"
        fh.write(latex_ele_mass.format(elements=ele_str))
    with open('isotope_abundances.tex', 'w') as fh:
        iso_str = ""
        flip = False
        for iso in sorted(used_isotopes_set):
            if iso in NATURAL_ABUNDANCE:
                iso_str += "{0} & {1} ".format(iso, NATURAL_ABUNDANCE[iso])
                if not flip:
                    iso_str += "& "
                    flip = True
                else:
                    iso_str += "\\\\\n"
                    flip = False
        if flip:
            ele_str += " & \\\\\n"
        fh.write(latex_nuc_abund.format(isotopes=iso_str))
    os.chdir(base)

if __name__ == "__main__":
  try:
    basedir = sys.argv[1]
  except:
    basedir = ".."

  write_materials(basedir)
