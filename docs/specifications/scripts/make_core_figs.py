#!/usr/bin/env python

from corefig import CoreFig

import sys
import os

try:
  base = sys.argv[1]
except:
  base = ".."


################################################################################
################################################################################
################################################################################

caption = "Control rod and shutdown bank positions. Source: \\ref{num:assycore}"
altcap = "Control rod and shutdown bank positions."
label = "fig_cr_pos"
out = os.path.join(base,"specifications{0}core{0}figs{0}cat_cr_pos".format(os.sep))

fig = CoreFig(caption,label,altcap=altcap)

fig.set_pos('M2','$\mathrm{S}_\mathrm{A}$')
fig.set_pos('K2','$\mathrm{B}$')
fig.set_pos('H2','$\mathrm{C}$')
fig.set_pos('F2','$\mathrm{B}$')
fig.set_pos('D2','$\mathrm{S}_\mathrm{A}$')

fig.set_pos('L3','$\mathrm{S}_\mathrm{D}$')
fig.set_pos('J3','$\mathrm{S}_\mathrm{B}$')
fig.set_pos('G3','$\mathrm{S}_\mathrm{B}$')
fig.set_pos('E3','$\mathrm{S}_\mathrm{C}$')

fig.set_pos('P4','$\mathrm{S}_\mathrm{A}$')
fig.set_pos('M4','$\mathrm{D}$')
fig.set_pos('H4','$\mathrm{S}_\mathrm{E}$')
fig.set_pos('D4','$\mathrm{D}$')
fig.set_pos('B4','$\mathrm{S}_\mathrm{A}$')

fig.set_pos('N5','$\mathrm{S}_\mathrm{C}$')
fig.set_pos('C5','$\mathrm{S}_\mathrm{D}$')

fig.set_pos('P6','$\mathrm{B}$')
fig.set_pos('K6','$\mathrm{C}$')
fig.set_pos('H6','$\mathrm{A}$')
fig.set_pos('F6','$\mathrm{C}$')
fig.set_pos('B6','$\mathrm{B}$')

fig.set_pos('N7','$\mathrm{S}_\mathrm{B}$')
fig.set_pos('C7','$\mathrm{S}_\mathrm{B}$')

fig.set_pos('P8','$\mathrm{C}$')
fig.set_pos('M8','$\mathrm{S}_\mathrm{E}$')
fig.set_pos('K8','$\mathrm{A}$')
fig.set_pos('H8','$\mathrm{D}$')
fig.set_pos('F8','$\mathrm{A}$')
fig.set_pos('D8','$\mathrm{S}_\mathrm{E}$')
fig.set_pos('B8','$\mathrm{C}$')

fig.set_pos('N9','$\mathrm{S}_\mathrm{B}$')
fig.set_pos('C9','$\mathrm{S}_\mathrm{B}$')

fig.set_pos('P10','$\mathrm{B}$')
fig.set_pos('K10','$\mathrm{C}$')
fig.set_pos('H10','$\mathrm{A}$')
fig.set_pos('F10','$\mathrm{C}$')
fig.set_pos('B10','$\mathrm{B}$')

fig.set_pos('N11','$\mathrm{S}_\mathrm{D}$')
fig.set_pos('C11','$\mathrm{S}_\mathrm{C}$')

fig.set_pos('P12','$\mathrm{S}_\mathrm{A}$')
fig.set_pos('M12','$\mathrm{D}$')
fig.set_pos('H12','$\mathrm{S}_\mathrm{E}$')
fig.set_pos('D12','$\mathrm{D}$')
fig.set_pos('B12','$\mathrm{S}_\mathrm{A}$')

fig.set_pos('L13','$\mathrm{S}_\mathrm{C}$')
fig.set_pos('J13','$\mathrm{S}_\mathrm{B}$')
fig.set_pos('G13','$\mathrm{S}_\mathrm{B}$')
fig.set_pos('E13','$\mathrm{S}_\mathrm{D}$')

fig.set_pos('M14','$\mathrm{S}_\mathrm{A}$')
fig.set_pos('K14','$\mathrm{B}$')
fig.set_pos('H14','$\mathrm{C}$')
fig.set_pos('F14','$\mathrm{B}$')
fig.set_pos('D14','$\mathrm{S}_\mathrm{A}$')

fig.write_fig(out+'.tex')

################################################################################

caption = "Instrument tube positions. Source: \\ref{num:instr_locs}"
altcap = "Instrument tube positions."
label = "fig_instr_pos"
out = os.path.join(base,"specifications{0}core{0}figs{0}cat_instr_pos".format(os.sep))

fig = CoreFig(caption,label,altcap=altcap)

fig.set_pos('J1','$\circ$')
fig.set_pos('F1','$\circ$')

fig.set_pos('N2','$\circ$')
fig.set_pos('K2','$\circ$')
fig.set_pos('H2','$\circ$')

fig.set_pos('H3','$\circ$')
fig.set_pos('F3','$\circ$')
fig.set_pos('D3','$\circ$')
fig.set_pos('B3','$\circ$')

fig.set_pos('P4','$\circ$')
fig.set_pos('N4','$\circ$')
fig.set_pos('H4','$\circ$')

fig.set_pos('L5','$\circ$')
fig.set_pos('G5','$\circ$')
fig.set_pos('E5','$\circ$')
fig.set_pos('C5','$\circ$')

fig.set_pos('R6','$\circ$')
fig.set_pos('N6','$\circ$')
fig.set_pos('K6','$\circ$')
fig.set_pos('H6','$\circ$')
fig.set_pos('B6','$\circ$')

fig.set_pos('M7','$\circ$')
fig.set_pos('J7','$\circ$')
fig.set_pos('F7','$\circ$')
fig.set_pos('C7','$\circ$')

fig.set_pos('R8','$\circ$')
fig.set_pos('N8','$\circ$')
fig.set_pos('L8','$\circ$')
fig.set_pos('J8','$\circ$')
fig.set_pos('F8','$\circ$')
fig.set_pos('D8','$\circ$')
fig.set_pos('C8','$\circ$')
fig.set_pos('B8','$\circ$')

fig.set_pos('P9','$\circ$')
fig.set_pos('G9','$\circ$')
fig.set_pos('E9','$\circ$')
fig.set_pos('A9','$\circ$')

fig.set_pos('L10','$\circ$')
fig.set_pos('J10','$\circ$')
fig.set_pos('D10','$\circ$')

fig.set_pos('R11','$\circ$')
fig.set_pos('L11','$\circ$')
fig.set_pos('H11','$\circ$')
fig.set_pos('E11','$\circ$')
fig.set_pos('A11','$\circ$')

fig.set_pos('K12','$\circ$')
fig.set_pos('G12','$\circ$')
fig.set_pos('D12','$\circ$')

fig.set_pos('N13','$\circ$')
fig.set_pos('L13','$\circ$')
fig.set_pos('H13','$\circ$')
fig.set_pos('B13','$\circ$')

fig.set_pos('N14','$\circ$')
fig.set_pos('J14','$\circ$')
fig.set_pos('F14','$\circ$')
fig.set_pos('D14','$\circ$')

fig.set_pos('L15','$\circ$')
fig.set_pos('H15','$\circ$')

fig.write_fig(out+'.tex')

################################################################################

# Cycle 1

caption = "Layout of fuel assemblies showing enrichment loading pattern and burnable absorber positions in cycle 1. Source: \\ref{num:assycore}"
altcap = "Cycle 1 core enrichment zones and burnable absorber positions"
label = "fig_enr_ba_pos"
out = os.path.join(base,"specifications{0}core{0}figs{0}cat_enr_ba_zones".format(os.sep))

fig = CoreFig(caption,label,altcap=altcap)

fig.set_legend()

fig.set_pos('K1','6',hyper='ass_6ba_target')
fig.set_pos('H1','6',hyper='ass_6ba_target')
fig.set_pos('F1','6',hyper='ass_6ba_target')

fig.set_pos('L2','16',hyper='ass_16ba_target')
fig.set_pos('J2','20',hyper='ass_20ba_target')
fig.set_pos('G2','20',hyper='ass_20ba_target')
fig.set_pos('E2','16',hyper='ass_16ba_target')

fig.set_pos('N3','15',hyper='ass_15ba_target')
fig.set_pos('M3','16',hyper='ass_16ba_target')
fig.set_pos('K3','16',hyper='ass_16ba_target')
fig.set_pos('H3','16',hyper='ass_16ba_target')
fig.set_pos('F3','16',hyper='ass_16ba_target')
fig.set_pos('D3','16',hyper='ass_16ba_target')
fig.set_pos('C3','15',hyper='ass_15ba_target')

fig.set_pos('N4','16',hyper='ass_16ba_target')
fig.set_pos('L4','16',hyper='ass_16ba_target')
fig.set_pos('J4','12',hyper='ass_12ba_target')
fig.set_pos('G4','12',hyper='ass_12ba_target')
fig.set_pos('E4','16',hyper='ass_16ba_target')
fig.set_pos('C4','16',hyper='ass_16ba_target')

fig.set_pos('P5','16',hyper='ass_16ba_target')
fig.set_pos('M5','16',hyper='ass_16ba_target')
fig.set_pos('K5','12',hyper='ass_12ba_target')
fig.set_pos('H5','12',hyper='ass_12ba_target')
fig.set_pos('F5','12',hyper='ass_12ba_target')
fig.set_pos('D5','16',hyper='ass_16ba_target')
fig.set_pos('B5','16',hyper='ass_16ba_target')

fig.set_pos('R6','6',hyper='ass_6ba_target')
fig.set_pos('N6','16',hyper='ass_16ba_target')
fig.set_pos('L6','12',hyper='ass_12ba_target')
fig.set_pos('J6','12',hyper='ass_12ba_target')
fig.set_pos('G6','12',hyper='ass_12ba_target')
fig.set_pos('E6','12',hyper='ass_12ba_target')
fig.set_pos('C6','16',hyper='ass_16ba_target')
fig.set_pos('A6','6',hyper='ass_6ba_target')

fig.set_pos('P7','20',hyper='ass_20ba_target')
fig.set_pos('M7','12',hyper='ass_12ba_target')
fig.set_pos('K7','12',hyper='ass_12ba_target')
fig.set_pos('H7','16',hyper='ass_16ba_target')
fig.set_pos('F7','12',hyper='ass_12ba_target')
fig.set_pos('D7','12',hyper='ass_12ba_target')
fig.set_pos('B7','20',hyper='ass_20ba_target')

fig.set_pos('R8','6',hyper='ass_6ba_target')
fig.set_pos('N8','16',hyper='ass_16ba_target')
fig.set_pos('L8','12',hyper='ass_12ba_target')
fig.set_pos('J8','16',hyper='ass_16ba_target')
fig.set_pos('G8','16',hyper='ass_16ba_target')
fig.set_pos('E8','12',hyper='ass_12ba_target')
fig.set_pos('C8','16',hyper='ass_16ba_target')
fig.set_pos('A8','6',hyper='ass_6ba_target')

fig.set_pos('P9','20',hyper='ass_20ba_target')
fig.set_pos('M9','12',hyper='ass_12ba_target')
fig.set_pos('K9','12',hyper='ass_12ba_target')
fig.set_pos('H9','16',hyper='ass_16ba_target')
fig.set_pos('F9','12',hyper='ass_12ba_target')
fig.set_pos('D9','12',hyper='ass_12ba_target')
fig.set_pos('B9','20',hyper='ass_20ba_target')

fig.set_pos('R10','6',hyper='ass_6ba_target')
fig.set_pos('N10','16',hyper='ass_16ba_target')
fig.set_pos('L10','12',hyper='ass_12ba_target')
fig.set_pos('J10','12',hyper='ass_12ba_target')
fig.set_pos('G10','12',hyper='ass_12ba_target')
fig.set_pos('E10','12',hyper='ass_12ba_target')
fig.set_pos('C10','16',hyper='ass_16ba_target')
fig.set_pos('A10','6',hyper='ass_6ba_target')

fig.set_pos('P11','16',hyper='ass_16ba_target')
fig.set_pos('M11','16',hyper='ass_16ba_target')
fig.set_pos('K11','12',hyper='ass_12ba_target')
fig.set_pos('H11','12',hyper='ass_12ba_target')
fig.set_pos('F11','12',hyper='ass_12ba_target')
fig.set_pos('D11','16',hyper='ass_16ba_target')
fig.set_pos('B11','16',hyper='ass_16ba_target')

fig.set_pos('N12','16',hyper='ass_16ba_target')
fig.set_pos('L12','16',hyper='ass_16ba_target')
fig.set_pos('J12','12',hyper='ass_12ba_target')
fig.set_pos('G12','12',hyper='ass_12ba_target')
fig.set_pos('E12','16',hyper='ass_16ba_target')
fig.set_pos('C12','16',hyper='ass_16ba_target')

fig.set_pos('N13','15',hyper='ass_15ba_target')
fig.set_pos('M13','16',hyper='ass_16ba_target')
fig.set_pos('K13','16',hyper='ass_16ba_target')
fig.set_pos('H13','16',hyper='ass_16ba_target')
fig.set_pos('F13','16',hyper='ass_16ba_target')
fig.set_pos('D13','16',hyper='ass_16ba_target')
fig.set_pos('C13','15',hyper='ass_15ba_target')

fig.set_pos('L14','16',hyper='ass_16ba_target')
fig.set_pos('J14','20',hyper='ass_20ba_target')
fig.set_pos('G14','20',hyper='ass_20ba_target')
fig.set_pos('E14','16',hyper='ass_16ba_target')

fig.set_pos('K15','6',hyper='ass_6ba_target')
fig.set_pos('H15','6',hyper='ass_6ba_target')
fig.set_pos('F15','6',hyper='ass_6ba_target')

fig.write_fig(out+'.tex')

################################################################################

# Cycle 2

caption = "Cycle 2 shuffling pattern, burnable absorber positions, and enrichment loading pattern of fresh assemblies. Sources: \\ref{num:assycore}, \\ref{num:c2shuffle}"
altcap = "Cycle 2 shuffling pattern and burnable absorber positions"
label = "fig_enr_ba_pos_c2"
out = os.path.join(base,"specifications{0}core{0}figs{0}cat_enr_ba_zones_c2".format(os.sep))

fig = CoreFig(caption,label,altcap=altcap)

fig.set_cycle_2(True)
fig.set_legend()

# pasted from excel spreadsheet
a = """                         L10     F       F       F       F       F       E10                             
                G10     F       F       L02     P12     N03     B12     E02     F       F       J10             
        F09     F       N02     N10     F       D11     R10     M11     F       C10     C02     F       K09     
        F       P03     L08     F       M09     E15     G08     L15     D09     F       H05     B03     F       
F05     F       F03     F       M04     F       M03     A10     D03     F       D04     F       K03     F       K05
F       P05     F       G04     F       N08     R09     G14     A09     H03     F       J04     F       B05     F
F       D02     E12     A11     N04     G01     B09     H15     J14     J01     C04     R11     L12     M02     F
F       N13     F15     H07     F01     B07     A08     F14     R08     P09     K15     H09     K01     C03     F
F       D14     E04     A05     N12     G15     G02     H01     P07     J15     C12     R05     L04     M14     F
F       P11     F       G12     F       H13     R07     J02     A07     C08     F       J12     F       B11     F
F11     F       F13     F       M12     F       M13     R06     D13     F       D12     F       K13     F       K11
        F       P13     H11     F       M07     E01     J08     L01     D07     F       E08     B13     F       
        F07     F       N14     N06     F       D05     A06     M05     F       C06     C14     F       K07     
                G06     F       F       L14     P04     C13     B04     E14     F       F       J06             
                                L06     F       F       F       F       F       E06                             """

col2lett = { 1:"R", 2:"P", 3:"N", 4:"M", 5:"L", 6:"K", 7:"J", 8:"H", 9:"G", 10:"F", 11:"E", 12:"D", 13:"C", 14:"B", 15:"A" }
col_offsets = {1:4, 2:2, 3:1, 4:1, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:1, 13:1, 14:2, 15:4}

labels = {}
for r in range(1,16):
  for c in range(1,16):
    labels[(r,c)] = "{}{}".format(col2lett[c],r)

ba4 = ["E14","B11",  "L14","P11",  "P5","L2",   "E2","B5"]
ba8 = ["F11","E10","E6","F5","K5","L6","L10","K11", "F13","C10","C6","F3","K3","N6","N10","K13"]
ba12 = ["E12","D11","D5","E4","L4","M5","M11","L12"]

for r,line in enumerate(a.split('\n')):
  cols = line.split()
  for c, val in enumerate(cols):
    co = col_offsets[r+1]
    pos = labels[(r+1,c+1+co)]

    if val == "F":
      if pos in ba4:
        fig.set_pos(pos,"\small {0}".format(4),hyper='ass_4ba_target')
      elif pos in ba8:
        fig.set_pos(pos,"\small {0}".format(8),hyper='ass_8ba_target')
      elif pos in ba12:
        fig.set_pos(pos,"\small {0}".format(12),hyper='ass_12ba_c2_target')
      else:
        fig.set_pos(pos,'')
    else:
      fig.set_pos(pos,"\\scriptsize {0}".format(val))

fig.write_fig(out+'.tex')

