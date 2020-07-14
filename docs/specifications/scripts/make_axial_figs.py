#!/usr/bin/env python

from __future__ import division

import sys
import os

fig_t = r"""\begin{{figure}}[htbp]
    \centering
    \begin{{tikzpicture}}[scale={scale},x=1in,y=1in]{tikzpic}
{matrix}
    \end{{tikzpicture}}


    \caption[{shortcap}]{{{caption}\label{{{label}}}}}
\end{{figure}}"""

matrix_t = r"""     \matrix [matrix of nodes,row sep=0,column sep=0]
      {{{rows}
      }};
"""

row_t = """\n       \draw (-1,{bot}) rectangle (1,{top}); & {fill} \\\\"""

## <!--- axials copied straight from rod_axials.ods
# Core Structures			
struct_LowestExtent           	=	   "0.00000"	 # 
struct_SupportPlate_bot       	=	   "20.0000"	 # arbitrary amount of water below core
struct_SupportPlate_top       	=	   "25.0000"	 # guessed
struct_LowerNozzle_bot        	=	   "25.0000"	 # same as struct_SupportPlate_top
struct_LowerNozzle_top        	=	   "35.0000"	 # approx from ** NDR of 4.088in for lower nozzle height
struct_UpperNozzle_bot        	=	   "423.049"	 # fig 4.2-3 from Watts Bar Unit 2 safety analysis report
struct_UpperNozzle_top        	=	   "431.876"	 # fig 4.2-3 from Watts Bar Unit 2 safety analysis report
struct_HighestExtent          	=	   "460.000"	 # arbitrary amount of water above core
                              			
# Fuel Rod			
fuel_Rod_bot                  	=	   "35.0000"	 # same as struct_LowerNozzle_top
fuel_LowerFitting_bot         	=	   "35.0000"	 # ML033530020 Fig 2-7
fuel_LowerFitting_top         	=	   "36.7480"	 # ML033530020 Fig 2-7
fuel_ActiveFuel_bot           	=	   "36.7480"	 # ML033530020 Fig 2-7
fuel_ActiveFuel_top           	=	   "402.508"	 # ML033530020 Fig 2-7
fuel_Plenum_bot               	=	   "402.508"	 # ML033530020 Fig 2-7
fuel_Plenum_top               	=	   "417.164"	 # ML033530020 Fig 2-7
fuel_UpperFitting_bot         	=	   "417.164"	 # ML033530020 Fig 2-7
fuel_UpperFitting_top         	=	   "419.704"	 # ML033530020 Fig 2-7
fuel_Rod_top                  	=	   "419.704"	 # ML033530020 Fig 2-7
                              			
# RCCAs (0 steps withdraw, i.e., fully inserted)			
rcca_Rod_bot                  	=	   "39.9580"	 # ML033530020 Fig 2-8
rcca_LowerFitting_bot         	=	   "39.9580"	 # ML033530020 Fig 2-8
rcca_LowerFitting_top         	=	   "41.8280"	 # ML033530020 Fig 2-8
rcca_AIC_bot                  	=	   "41.8280"	 # ML033530020 Fig 2-8
rcca_AIC_top                  	=	   "143.428"	 # ML033530020 Fig 2-8
rcca_B4C_bot                  	=	   "143.428"	 # ML033530020 Fig 2-8
rcca_B4C_top                  	=	   "402.508"	 # ML033530020 Fig 2-8
rcca_Spacer_bot               	=	   "402.508"	 # ML033530020 Fig 2-8
rcca_Spacer_top               	=	   "403.778"	 # ML033530020 Fig 2-8
rcca_Plenum_bot               	=	   "403.778"	 # ML033530020 Fig 2-8
rcca_Plenum_top               	=	   "415.558"	 # ML033530020 Fig 2-8
rcca_Rod_top                  	=	   "460.000"	 # same as struct_HighestExtent
rcca_StepWidth                	=	   "1.58193"	 # Active height divided into 228 steps
                              			
# BPRAs                       			
bpra_Rod_bot                  	=	   "38.6600"	 # ML033530020 Fig 2-9
bpra_LowerFitting_bot         	=	   "38.6600"	 # ML033530020 Fig 2-9
bpra_LowerFitting_top         	=	   "40.5580"	 # ML033530020 Fig 2-9
bpra_Active_bot               	=	   "40.5580"	 # ML033530020 Fig 2-9
bpra_Active_top               	=	   "401.238"	 # ML033530020 Fig 2-9
bpra_Plenum_bot               	=	   "401.238"	 # ML033530020 Fig 2-9
bpra_Plenum_top               	=	   "421.532"	 # ML033530020 Fig 2-9
bpra_Rod_top                  	=	   "431.876"	 # same as struct_UpperNozzle_top
                              			
# Guide Tube                  			
gt_Rod_bot                    	=	   "35.0000"	 # same as fuel_Rod_bot
gt_Dashpot_bot                	=	   "35.0000"	 # 
gt_Dashpot_top                	=	   "39.9580"	 # same as rcca_Rod_bot for full insertion
gt_Upper_bot                  	=	   "39.9580"	 # 
gt_Upper_top                  	=	   "423.049"	 # same as struct_UpperNozzle_bot
gt_Rod_top                    	=	   "423.049"	 # 
                              			
# Intrument Tube              			
instr_Rod_bot                 	=	   "35.0000"	 # same as fuel_Rod_bot
instr_Rod_top                 	=	   "423.049"	 # same as struct_UpperNozzle_bot
                              			
# Grid Spacers (centers provided by utiliy)  (heights 1.65 top/bottom, 2.25 intermediate) 			
grid1_bot                     	=	   "37.1621"	 # 
grid1_top                     	=	   "40.5200"	 # 
grid2_bot                     	=	   "98.0250"	 # 
grid2_top                     	=	   "103.740"	 # 
grid3_bot                     	=	   "150.222"	 # 
grid3_top                     	=	   "155.937"	 # 
grid4_bot                     	=	   "202.419"	 # 
grid4_top                     	=	   "208.134"	 # 
grid5_bot                     	=	   "254.616"	 # 
grid5_top                     	=	   "260.331"	 # 
grid6_bot                     	=	   "306.813"	 # 
grid6_top                     	=	   "312.528"	 # 
grid7_bot                     	=	   "359.010"	 # 
grid7_top                     	=	   "364.725"	 # 
grid8_bot                     	=	   "411.806"	 # 
grid8_top                     	=	   "415.164"	 # 

## -- axials copied straight from rod_axials.ods -->

# order doesn't matter here: this will be put into a dictionary
all_planes= [ ['Lowest Extent', struct_LowestExtent],
              ['Bottom of Support Plate', struct_SupportPlate_bot],
              ['Top of Support Plate', struct_SupportPlate_top],
              ['Bottom of Fuel Rod', fuel_Rod_bot],
              ['Bottom of Active Fuel', fuel_ActiveFuel_bot],
              ['Grid 1 Bottom', grid1_bot],
              ['Bot. of BPRA Rod', bpra_Rod_bot],
              ['Control Rod Step 0', rcca_Rod_bot],
              ['Bottom of Active Absorber', bpra_Active_bot],
              ['Grid 1 Top', grid1_top],
              ['Grid 2 Bottom', grid2_bot],
              ['Grid 2 Top', grid2_top],
              ['Grid 3 Bottom', grid3_bot],
              ['Grid 3 Top', grid3_top],
              ['Grid 4 Bottom', grid4_bot],
              ['Grid 4 Top', grid4_top],
              ['Grid 5 Bottom', grid5_bot],
              ['Grid 5 Top', grid5_top],
              ['Grid 6 Bottom', grid6_bot],
              ['Grid 6 Top', grid6_top],
              ['Grid 7 Bottom', grid7_bot],
              ['Grid 7 Top', grid7_top],
              ['Top of Active Absorber', bpra_Active_top],
              ['Top of Active Fuel', fuel_ActiveFuel_top],
              ['Control Rod Step 228', '{:.6g}'.format(float(rcca_StepWidth)*228+float(rcca_Rod_bot))],
              ['Grid 8 Bottom', grid8_bot],
              ['Grid 8 Top', grid8_top],
              ['Top of Fuel Rod Plenum', fuel_UpperFitting_bot],
              ['Top of BPRA Rod Plenum', bpra_Plenum_top],
              ['Top of Fuel Rod', fuel_Rod_top],
              ['Bottom of Upper Nozzle', struct_UpperNozzle_bot],
              ['Top of Upper Nozzle', struct_UpperNozzle_top],
              ['Highest Extent', struct_HighestExtent],]

all_planes += [['Bottom of Lower Absorber (AIC)', rcca_AIC_bot],
              ['Bottom of Upper Absorber (B4C)', rcca_B4C_bot],
              ['Bottom of Spacer', rcca_Spacer_bot],
              ['Bottom of Control Rod Plenum', rcca_Plenum_bot],
              ['Top of Control Rod Plenum', rcca_Plenum_top],]

# convert into a dictionary for use in figures
d = {}
d.update(all_planes)
all_planes = d

def main(base):

  make_aggregate_fig(base)
  make_fuel_rod(base)
  make_gtu_rod(base)
  make_instr_rod(base)
  make_ba_rod(base)
  make_cr_rod(base)


def make_aggregate_fig(base):

  outp = os.path.join(base,"specifications{0}axial{0}figs{0}all_axials.tex".format(os.sep))

  cap = "\emph{Left}: Scale view of row 8 axial cross section, with highlighted grid spacers and partial insertion of control rod bank D to the bite position. \emph{Right}: exhaustive list of all axial planes used in the model, excluding partial control rod insertion planes."
  scap = "Scale view of all axial planes."
  l = "fig_all_axials"
  s = 1

  # if the planes change, this is the only place to update them

  axials = [ 'Lowest Extent',
             'Bottom of Support Plate',
             'Bottom of Fuel Rod',
             'Bottom of Active Fuel',
             'Grid 1 Bottom',
             'Bot. of BPRA Rod',
             'Control Rod Step 0',
             'Grid 1 Top',
             'Bottom of Active Absorber',
             'Bottom of Lower Absorber (AIC)',
             'Grid 2 Bottom',
             'Grid 2 Top',
             'Grid 3 Bottom',
             'Grid 3 Top',
             'Grid 4 Bottom',
             'Grid 4 Top',
             'Grid 5 Bottom',
             'Grid 5 Top',
             'Grid 6 Bottom',
             'Grid 6 Top',
             'Grid 7 Bottom',
             'Grid 7 Top',
             'Control Rod Step 228',
             'Top of Active Absorber',
             'Top of Active Fuel',
             'Bottom of Control Rod Plenum',
             'Grid 8 Bottom',
             'Grid 8 Top',
             'Top of Control Rod Plenum',
             'Top of Fuel Rod Plenum',
             'Top of Fuel Rod',
             'Top of BPRA Rod Plenum',
             'Bottom of Upper Nozzle',
             'Top of Upper Nozzle',
             'Highest Extent']

  # get ordered list
  axials = [[a,all_planes[a]] for a in axials]

  # desired figure height
  figH = 4.0

  # actual figure dimentions in inches
  picH = 27.774
  picW = 27.774

  figW = figH*picW/picH

  barrelIR = 161.2773*figH/float(axials[-1][1])

  tikzpic = r"""
      \draw[white] (-{1},-{2}) rectangle ({1},{2});
      \node {{\pgftext{{\includegraphics[width={0}in]{{specifications/axial/figs/row_8_mats_axial_grids_enhanced.png}}}}}};""".format(
        figW,figW/2,figH/2)
  for i,ax in enumerate(axials):
    tikzpic += "\n      \draw[red] ({0},{1}) -- ({2},{1}) -- ({3},{4}) -- ({6},{4}) node[black,right,anchor=west,font=\scriptsize] {{{5}}};".format(
                                                                      barrelIR,
                                                                      float(ax[1])*figH/float(axials[-1][1])-figH/2,
                                                                      figW/2+0.2,
                                                                      figW/2+0.4,
                                                                      figH*i/(len(axials)-1)-figH/2,
                                                                      "~{0} ~~~~~~~~ {1}".format(ax[1],ax[0]),
                                                                      figW/2+0.55)
  tikzpic += "\n      \draw ({0},{1}) node[left,anchor=west,font=\scriptsize] {{\underline{{Elevation (cm)}} ~~~ \underline{{Description}}}};".format(figW/2+0.4,figH/2 + figH/(len(axials)-1))
    
  mat = ""
  

  
  outStr = fig_t.format(tikzpic=tikzpic,matrix=mat,shortcap=scap,caption=cap,label=l,scale=s)
  
  with open(outp,'w') as fh:
    fh.write(outStr)



def make_fuel_rod(base):

  outp = os.path.join(base,"specifications{0}axial{0}figs{0}fuel_rod.tex".format(os.sep))

  cap = "Fuel rod pincell axial specification."
  scap = "Fuel rod pincell axial specification"
  l = "fig_fuel_axials"
  s = 1
  
  figH = 5.0
  width = 3

  # the third entry is the text above the specified plane
  ## changed so the axial height here isn't used - the global all_planes is
  axials = [  ['Lowest Extent', '0', 'Water', 'mat_water', r""],
              ['Bottom of Support Plate', '50.8', 'Nozzle / Support Plate Stainless Steel', 'mat_ss_spn', r"\ref{num:missing}"],
              ['Bottom of Fuel Rod', '66.18352', 'Zircaloy Pin', 'mat_zirc', r"\ref{num:catawba}"],
              ['Bottom of Active Fuel', '67.02172', 'Fuel Rod Pincell', 'fig_fuel_pin', r"\ref{num:fuelheight}"],
              ['Grid 1 Bottom', '68.16472', 'Fuel Rod Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 1 Top', '71.5226', 'Fuel Rod Pincell', 'fig_fuel_pin', r"\ref{num:fuelheight}"],
              ['Grid 2 Bottom', '130.21692', 'Fuel Rod Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 2 Top', '133.5748', 'Fuel Rod Pincell', 'fig_fuel_pin', r"\ref{num:fuelheight}"],
              ['Grid 3 Bottom', '182.41392', 'Fuel Rod Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 3 Top', '185.7718', 'Fuel Rod Pincell', 'fig_fuel_pin', r"\ref{num:fuelheight}"],
              ['Grid 4 Bottom', '234.61092', 'Fuel Rod Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 4 Top', '237.9688', 'Fuel Rod Pincell', 'fig_fuel_pin', r"\ref{num:fuelheight}"],
              ['Grid 5 Bottom', '286.80792', 'Fuel Rod Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 5 Top', '290.1658', 'Fuel Rod Pincell', 'fig_fuel_pin', r"\ref{num:fuelheight}"],
              ['Grid 6 Bottom', '339.00492', 'Fuel Rod Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 6 Top', '342.3628', 'Fuel Rod Pincell', 'fig_fuel_pin', r"\ref{num:fuelheight}"],
              ['Grid 7 Bottom', '391.20192', 'Fuel Rod Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 7 Top', '394.5598', 'Fuel Rod Pincell', 'fig_fuel_pin', r"\ref{num:fuelheight}"],
              ['Top of Active Fuel', '432.78172', 'Fuel Rod Plenum Pincell', 'fig_fuel_pin', r"\ref{num:catawba}"],
              ['Grid 8 Bottom', '443.50052', 'Fuel Rod Plenum Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 8 Top', '446.8584', 'Fuel Rod Plenum Pincell', 'fig_fuel_pin', r"\ref{num:catawba}"],
              ['Top of Fuel Rod Plenum', '452.23812', 'Zircaloy Pin', 'mat_zirc', r"\ref{num:catawba}"],
              ['Top of Fuel Rod', '454.29552', 'Water', 'mat_water', r"\ref{num:catawba}"],
              ['Bottom of Upper Nozzle', '457.6407', 'Nozzle / Support Plate Stainless Steel', 'mat_ss_spn', r"\ref{num:watts_bar}"],
              ['Top of Upper Nozzle', '466.4672', 'Water', 'mat_water', r"\ref{num:watts_bar}"],
              ['Highest Extent', '517.2672', 'Water', 'mat_water', ''],]
  axials = [[a[0],all_planes[a[0]],a[2],a[3],a[4]] for a in axials]

  mat = ""
  
  
  tikzpic = ""
  for i,ax in enumerate(axials[:-1]):
    tikzpic += """\n      \\node[inner sep=0pt,
        text width={w} in,
        minimum size={h} in,
        draw=black,
        align=center,
        shift={{(0,{s})}},
        hyperlink node={hyper}] (n{0}) {{{fill}}};""".format(i,fill=ax[2],w=width,h=figH/(len(axials)-1),s=i*figH/(len(axials)-1),hyper=ax[3])
    tikzpic += """\n      \draw[->] ({w2},{h}) node[right,anchor=west] {{{text}}} -- ({w},{h});""".format(w=width/2,h=(i-0.5)*figH/(len(axials)-1),w2=width/2+0.2,text="{0} ~~~~~~~ {1}".format(ax[1],ax[0]))
    tikzpic += """\n      \\node[anchor=east] (s{0}) at (n{0}.west) {{{1}}};""".format(i,ax[4])
  tikzpic += """\n      \\path let \p1 = (n{0}.west) in node[anchor=west] (source) at (\\x1,{h}) {{\underline{{Source Reference}}}};""".format(i,w=0,h=(len(axials)-0.5)*figH/(len(axials)-1),)
  tikzpic += """\n      \draw[->] (source.west) -| (s{0}.north);""".format(i)
  tikzpic += """\n      \draw[->] ({w2},{h}) node[right,anchor=west] {{{text}}} -- ({w},{h});""".format(w=width/2,h=(len(axials)-1.5)*figH/(len(axials)-1),w2=width/2+0.2,text="{0} ~~~~~~~ {1}".format(axials[-1][1],axials[-1][0]))
  tikzpic += """\n      \draw ({w},{h}) node[right,anchor=west] {{{text}}};""".format(w=width/2,h=(len(axials)-0.5)*figH/(len(axials)-1),
                                              text="\underline{Elevation (cm)} ~ \underline{Description}")

  outStr = fig_t.format(tikzpic=tikzpic,matrix=mat,shortcap=scap,caption=cap,label=l,scale=s)
  
  with open(outp,'w') as fh:
    fh.write(outStr)


def make_gtu_rod(base):

  outp = os.path.join(base,"specifications{0}axial{0}figs{0}guide_tube.tex".format(os.sep))

  cap = "Empty guide tube pincell axial specification."
  scap = "Empty guide tube pincell axial specification"
  l = "fig_gtu_axials"
  s = 1
  
  figH = 5.0
  width = 3

  # the third entry is the text above the specified plane
  ## changed so the axial height here isn't used - the global all_planes is
  axials = [  ['Lowest Extent', '0', 'Water', 'mat_water', r""],
              ['Bottom of Support Plate', '20.0', 'Nozzle / Support Plate Borated Water', 'mat_water_spn', r"\ref{num:missing}"],
              ['Bottom of Fuel Rod', '66.18352', 'Dashpot Guide Tube', 'fig_guidetube_da_pin', r"\ref{num:gtu_axials}"],
              ['Grid 1 Bottom', '68.16472', 'Dashpot Guide Tube w/ Grid', 'fig_guidetube_da_pin', r"\ref{num:gtu_axials}"],
              ['Control Rod Step 0', '71.5226', 'Guide Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 1 Top', '74.59092', 'Guide Tube Pincell', 'fig_guidetube_pin', r"\ref{num:gtu_axials}"],
              ['Grid 2 Bottom', '130.21692', 'Guide Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 2 Top', '133.5748', 'Guide Tube Pincell', 'fig_guidetube_pin', r"\ref{num:gtu_axials}"],
              ['Grid 3 Bottom', '182.41392', 'Guide Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 3 Top', '185.7718', 'Guide Tube Pincell', 'fig_guidetube_pin', r"\ref{num:gtu_axials}"],
              ['Grid 4 Bottom', '234.61092', 'Guide Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 4 Top', '237.9688', 'Guide Tube Pincell', 'fig_guidetube_pin', r"\ref{num:gtu_axials}"],
              ['Grid 5 Bottom', '286.80792', 'Guide Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 5 Top', '290.1658', 'Guide Tube Pincell', 'fig_guidetube_pin', r"\ref{num:gtu_axials}"],
              ['Grid 6 Bottom', '339.00492', 'Guide Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 6 Top', '342.3628', 'Guide Tube Pincell', 'fig_guidetube_pin', r"\ref{num:gtu_axials}"],
              ['Grid 7 Bottom', '391.20192', 'Guide Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 7 Top', '394.5598', 'Guide Tube Pincell', 'fig_guidetube_pin', r"\ref{num:gtu_axials}"],
              ['Grid 8 Bottom', '443.50052', 'Guide Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 8 Top', '446.8584', 'Guide Tube Pincell', 'fig_guidetube_pin', r"\ref{num:gtu_axials}"],
              ['Bottom of Upper Nozzle', '517.2672', 'Nozzle / Support Plate Borated Water', 'mat_water_spn', r"\ref{num:watts_bar}"],
              ['Top of Upper Nozzle', '517.2672', 'Water', 'mat_water', r"\ref{num:watts_bar}"],
              ['Highest Extent', '517.2672', 'Water', 'mat_water', ''],]
  axials = [[a[0],all_planes[a[0]],a[2],a[3],a[4]] for a in axials]

  mat = ""
  
  
  tikzpic = ""
  for i,ax in enumerate(axials[:-1]):
    tikzpic += """\n      \\node[inner sep=0pt,
        text width={w} in,
        minimum size={h} in,
        draw=black,
        align=center,
        shift={{(0,{s})}},
        hyperlink node={hyper}] (n{0}) {{{fill}}};""".format(i,fill=ax[2],w=width,h=figH/(len(axials)-1),s=i*figH/(len(axials)-1),hyper=ax[3])
    tikzpic += """\n      \draw[->] ({w2},{h}) node[right,anchor=west] {{{text}}} -- ({w},{h});""".format(w=width/2,h=(i-0.5)*figH/(len(axials)-1),w2=width/2+0.2,text="{0} ~~~~~~~ {1}".format(ax[1],ax[0]))
    tikzpic += """\n      \\node[anchor=east] (s{0}) at (n{0}.west) {{{1}}};""".format(i,ax[4])
  tikzpic += """\n      \\path let \p1 = (n{0}.west) in node[anchor=west] (source) at (\\x1,{h}) {{\underline{{Source Reference}}}};""".format(i,w=0,h=(len(axials)-0.5)*figH/(len(axials)-1),)
  tikzpic += """\n      \draw[->] (source.west) -| (s{0}.north);""".format(i)
  tikzpic += """\n      \draw ({w},{h}) node[right,anchor=west] {{{text}}};""".format(w=width/2,h=(len(axials)-0.5)*figH/(len(axials)-1),
                                              text="\underline{Elevation (cm)} ~ \underline{Description}")

  outStr = fig_t.format(tikzpic=tikzpic,matrix=mat,shortcap=scap,caption=cap,label=l,scale=s)


  with open(outp,'w') as fh:
    fh.write(outStr)


def make_instr_rod(base):

  outp = os.path.join(base,"specifications{0}axial{0}figs{0}instr_tube.tex".format(os.sep))

  cap = "Instrument tube pincell axial specification."
  scap = "Instrument tube pincell axial specification"
  l = "fig_instr_axials"
  s = 1
  
  figH = 5.0
  width = 3

  # the third entry is the text above the specified plane
  ## changed so the axial height here isn't used - the global all_planes is
  axials = [  ['Lowest Extent', '0', 'Bare Instr. Tube', 'fig_instr_pin_bare', r"\ref{num:instr_axials}"],
              ['Bottom of Support Plate', '20.0', 'Support Plate / Nozzle Borated Water', 'mat_water_spn', r"\ref{num:missing}"],
              ['Bottom of Fuel Rod', '66.18352', 'Instr. Tube Pincell', 'fig_instr_pin', r"\ref{num:instr_axials}"],
              ['Grid 1 Bottom', '68.16472', 'Instr. Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 1 Top', '71.5226', 'Instr. Tube Pincell', 'fig_instr_pin', r"\ref{num:instr_axials}"],
              ['Grid 2 Bottom', '130.21692', 'Instr. Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 2 Top', '133.5748', 'Instr. Tube Pincell', 'fig_instr_pin', r"\ref{num:instr_axials}"],
              ['Grid 3 Bottom', '182.41392', 'Instr. Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 3 Top', '185.7718', 'Instr. Tube Pincell', 'fig_instr_pin', r"\ref{num:instr_axials}"],
              ['Grid 4 Bottom', '234.61092', 'Instr. Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 4 Top', '237.9688', 'Instr. Tube Pincell', 'fig_instr_pin', r"\ref{num:instr_axials}"],
              ['Grid 5 Bottom', '286.80792', 'Instr. Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 5 Top', '290.1658', 'Instr. Tube Pincell', 'fig_instr_pin', r"\ref{num:instr_axials}"],
              ['Grid 6 Bottom', '339.00492', 'Instr. Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 6 Top', '342.3628', 'Instr. Tube Pincell', 'fig_instr_pin', r"\ref{num:instr_axials}"],
              ['Grid 7 Bottom', '391.20192', 'Instr. Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 7 Top', '394.5598', 'Instr. Tube Pincell', 'fig_instr_pin', r"\ref{num:instr_axials}"],
              ['Grid 8 Bottom', '443.50052', 'Instr. Tube Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 8 Top', '446.8584', 'Instr. Tube Pincell', 'fig_instr_pin', r"\ref{num:instr_axials}"],
              ['Bottom of Upper Nozzle', '517.2672', 'Water', 'mat_water', r"\ref{num:watts_bar}"],
              ['Highest Extent', '517.2672', '', '', ''],]
  axials = [[a[0],all_planes[a[0]],a[2],a[3],a[4]] for a in axials]

  mat = ""
  
  
  tikzpic = ""
  for i,ax in enumerate(axials[:-1]):
    tikzpic += """\n      \\node[inner sep=0pt,
        text width={w} in,
        minimum size={h} in,
        draw=black,
        align=center,
        shift={{(0,{s})}},
        hyperlink node={hyper}] (n{0}) {{{fill}}};""".format(i,fill=ax[2],w=width,h=figH/(len(axials)-1),s=i*figH/(len(axials)-1),hyper=ax[3])
    tikzpic += """\n      \draw[->] ({w2},{h}) node[right,anchor=west] {{{text}}} -- ({w},{h});""".format(w=width/2,h=(i-0.5)*figH/(len(axials)-1),w2=width/2+0.2,text="{0} ~~~~~~~ {1}".format(ax[1],ax[0]))
    tikzpic += """\n      \\node[anchor=east] (s{0}) at (n{0}.west) {{{1}}};""".format(i,ax[4])
  tikzpic += """\n      \\path let \p1 = (n{0}.west) in node[anchor=west] (source) at (\\x1,{h}) {{\underline{{Source Reference}}}};""".format(i,w=0,h=(len(axials)-0.5)*figH/(len(axials)-1),)
  tikzpic += """\n      \draw[->] (source.west) -| (s{0}.north);""".format(i)
  tikzpic += """\n      \draw[->] ({w2},{h}) node[right,anchor=west] {{{text}}} -- ({w},{h});""".format(w=width/2,h=(len(axials)-1.5)*figH/(len(axials)-1),w2=width/2+0.2,text="{0} ~~~~~~~ {1}".format(axials[-1][1],axials[-1][0]))
  tikzpic += """\n      \draw ({w},{h}) node[right,anchor=west] {{{text}}};""".format(w=width/2,h=(len(axials)-0.5)*figH/(len(axials)-1),
                                              text="\underline{Elevation (cm)} ~ \underline{Description}")

  outStr = fig_t.format(tikzpic=tikzpic,matrix=mat,shortcap=scap,caption=cap,label=l,scale=s)
  
  with open(outp,'w') as fh:
    fh.write(outStr)


def make_ba_rod(base):

  outp = os.path.join(base,"specifications{0}axial{0}figs{0}ba.tex".format(os.sep))

  cap = "Burnable absorber pincell axial specification."
  scap = "Burnable absorber pincell axial specification"
  l = "fig_ba_axials"
  s = 1
  
  figH = 6.0
  width = 3

  # the third entry is the text above the specified plane
  ## changed so the axial height here isn't used - the global all_planes is
  axials = [  ['Lowest Extent', '0', 'Water', 'mat_water', r""],
              ['Bottom of Support Plate', '20.0', 'Support Plate / Nozzle Borated Water', 'mat_water_spn', r"\ref{num:missing}"],
              ['Bottom of Fuel Rod', '', 'Dashpot Guide Tube', 'fig_guidetube_da_pin', r"\ref{num:gtu_axials}"],
              ['Grid 1 Bottom', '68.16472', 'Dashpot Guide Tube w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Bot. of BPRA Rod', '', 'SS Pin in Dashpot GT w/ Grid', 'mat_SS304', r"\ref{num:ba_axials}"],
              ['Control Rod Step 0', '74.59092', 'SS Pin in GT w/ Grid', 'mat_SS304', r"\ref{num:ba_axials}"],
              ['Grid 1 Top', '', 'Stainless Steel Pin in GT', 'mat_SS304', r"\ref{num:ba_axials}"],
              ['Bottom of Active Absorber', '', 'Burnable Absorber Pincell', 'fig_ba_pin', r"\ref{num:ba_axials}"],
              ['Grid 2 Bottom', '130.21692', 'Burnable Absorber Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 2 Top', '133.5748', 'Burnable Absorber Pincell', 'fig_ba_pin', r"\ref{num:ba_axials}"],
              ['Grid 3 Bottom', '182.41392', 'Burnable Absorber Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 3 Top', '185.7718', 'Burnable Absorber Pincell', 'fig_ba_pin', r"\ref{num:ba_axials}"],
              ['Grid 4 Bottom', '234.61092', 'Burnable Absorber Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 4 Top', '237.9688', 'Burnable Absorber Pincell', 'fig_ba_pin', r"\ref{num:ba_axials}"],
              ['Grid 5 Bottom', '286.80792', 'Burnable Absorber Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 5 Top', '290.1658', 'Burnable Absorber Pincell', 'fig_ba_pin', r"\ref{num:ba_axials}"],
              ['Grid 6 Bottom', '339.00492', 'Burnable Absorber Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 6 Top', '342.3628', 'Burnable Absorber Pincell', 'fig_ba_pin', r"\ref{num:ba_axials}"],
              ['Grid 7 Bottom', '391.20192', 'Burnable Absorber Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 7 Top', '394.5598', 'Burnable Absorber Pincell', 'fig_ba_pin', r"\ref{num:ba_axials}"],
              ['Top of Active Absorber', '', 'BPRA Rod Plenum Pincell', 'fig_ba_pin_plenum', r"\ref{num:ba_axials}"],
              ['Grid 8 Bottom', '443.50052', 'BPRA Rod Plenum Pincell w/ Grid', 'grid_spec', r"\ref{num:grid_spacer}"],
              ['Grid 8 Top', '446.8584', 'BPRA Rod Upper Plenum Pincell', 'fig_ba_pin_plenum', r"\ref{num:ba_axials}"],
              ['Top of BPRA Rod Plenum', '454.29552', 'Stainless Steel Pin in GT','mat_SS304', r"\ref{num:ba_axials}"],
              ['Bottom of Upper Nozzle', '', 'Stainless Steel Pin','mat_SS304', r"\ref{num:ba_axials}"],
              ['Top of Upper Nozzle', '454.29552', 'Water','mat_water', r"\ref{num:watts_bar}"],
              ['Highest Extent', '517.2672', '', '', ''],]
  axials = [[a[0],all_planes[a[0]],a[2],a[3],a[4]] for a in axials]

  mat = ""
  
  
  tikzpic = ""
  for i,ax in enumerate(axials[:-1]):
    tikzpic += """\n      \\node[inner sep=0pt,
        text width={w} in,
        minimum size={h} in,
        draw=black,
        align=center,
        shift={{(0,{s})}},
        hyperlink node={hyper}] (n{0}) {{{fill}}};""".format(i,fill=ax[2],w=width,h=figH/(len(axials)-1),s=i*figH/(len(axials)-1),hyper=ax[3])
    tikzpic += """\n      \draw[->] ({w2},{h}) node[right,anchor=west] {{{text}}} -- ({w},{h});""".format(w=width/2,h=(i-0.5)*figH/(len(axials)-1),w2=width/2+0.2,text="{0} ~~~~~~~ {1}".format(ax[1],ax[0]))
    tikzpic += """\n      \\node[anchor=east] (s{0}) at (n{0}.west) {{{1}}};""".format(i,ax[4])
  tikzpic += """\n      \\path let \p1 = (n{0}.west) in node[anchor=west] (source) at (\\x1,{h}) {{\underline{{Source Reference}}}};""".format(i,w=0,h=(len(axials)-0.5)*figH/(len(axials)-1),)
  tikzpic += """\n      \draw[->] (source.west) -| (s{0}.north);""".format(i)
  tikzpic += """\n      \draw[->] ({w2},{h}) node[right,anchor=west] {{{text}}} -- ({w},{h});""".format(w=width/2,h=(len(axials)-1.5)*figH/(len(axials)-1),w2=width/2+0.2,text="{0} ~~~~~~~ {1}".format(axials[-1][1],axials[-1][0]))
  tikzpic += """\n      \draw ({w},{h}) node[right,anchor=west] {{{text}}};""".format(w=width/2,h=(len(axials)-0.5)*figH/(len(axials)-1),
                                              text="\underline{Elevation (cm)} ~ \underline{Description}")

  outStr = fig_t.format(tikzpic=tikzpic,matrix=mat,shortcap=scap,caption=cap,label=l,scale=s)
  
  with open(outp,'w') as fh:
    fh.write(outStr)


def make_cr_rod(base):

  outp = os.path.join(base,"specifications{0}axial{0}figs{0}cr.tex".format(os.sep))

  cap = "Control rod pincell axial specification when fully-inserted.  This only shows axial sections for the control rod itself, which is inside one of the guide tubes."
  scap = "Control rod pincell axial specification"
  l = "fig_cr_axials"
  s = 1
  
  figH = 2.0
  width = 3.4

  # the third entry is the text above the specified plane
  ## changed so the axial height here isn't used - the global all_planes is
  axials = [  ['Lowest Extent', '0', 'Water', 'mat_water', r""],
              ['Bottom of Support Plate', '20.0', 'Support Plate / Nozzle Borated Water', 'mat_water_spn', r"\ref{num:missing}"],
              ['Bottom of Fuel Rod', '66.18352', 'Water', 'mat_water', r""],
              ['Control Rod Step 0', '', 'Stainless Steel Pin', 'mat_SS304', r"\ref{num:control_rod_axials}"],
              ['Bottom of Lower Absorber (AIC)', '', 'Control Rod Lower Absorber Pincell', 'fig_cr_pin', r"\ref{num:control_rod_axials}"],
              ['Bottom of Upper Absorber (B4C)', '', 'Control Rod Upper Absorber Pincell', 'fig_cr_pin_upper', r"\ref{num:control_rod_axials}"],
              ['Bottom of Spacer', '', 'Control Rod Spacer Pincell', 'fig_cr_pin_spacer', r"\ref{num:control_rod_axials}"],
              ['Bottom of Control Rod Plenum', '', 'Control Rod Upper Plenum', 'fig_cr_pin_plenum', r"\ref{num:control_rod_axials}"],
              ['Top of Control Rod Plenum', '', 'Stainless Steel Pin', 'mat_SS304', r"\ref{num:control_rod_axials}"],
              ['Highest Extent', '517.2672', 'Water', 'mat_water', ''],]
  axials = [[a[0],all_planes[a[0]],a[2],a[3],a[4]] for a in axials]

  mat = ""
  
  tikzpic = ""
  for i,ax in enumerate(axials[:-1]):
    if ax[0] == 'Control Rod Step 0': ax[0] = 'Bottom of Control Rod'
    d = 'black'
    tikzpic += """\n      \\node[inner sep=0pt,
        text width={w} in,
        minimum size={h} in,
        draw={draw},
        align=center,
        shift={{(0,{s})}},
        hyperlink node={hyper}] (n{0}) {{{fill}}};""".format(i,fill=ax[2],w=width,h=figH/(len(axials)-1),s=i*figH/(len(axials)-1),hyper=ax[3],draw=d)
    tikzpic += """\n      \draw[->] ({w2},{h}) node[right,anchor=west] {{{text}}} -- ({w},{h});""".format(w=width/2,h=(i-0.5)*figH/(len(axials)-1),w2=width/2+0.2,text="{0} ~~~~~~~ {1}".format(ax[1],ax[0]))
    tikzpic += """\n      \\node[anchor=east] (s{0}) at (n{0}.west) {{{1}}};""".format(i,ax[4])
  tikzpic += """\n      \\path let \p1 = (n{0}.west) in node[anchor=west] (source) at (\\x1,{h}) {{\underline{{Source Reference}}}};""".format(i,w=0,h=(len(axials)-0.5)*figH/(len(axials)-1),)
  tikzpic += """\n      \draw[->] (source.west) -| (s{0}.north);""".format(i)
  tikzpic += """\n      \draw[->] ({w2},{h}) node[right,anchor=west] {{{text}}} -- ({w},{h});""".format(w=width/2,h=(len(axials)-1.5)*figH/(len(axials)-1),w2=width/2+0.2,text="{0} ~~~~~~~ {1}".format(axials[-1][1],axials[-1][0]))
  tikzpic += """\n      \draw ({w},{h}) node[right,anchor=west] {{{text}}};""".format(w=width/2,h=(len(axials)-0.5)*figH/(len(axials)-1),
                                              text="\underline{Elevation (cm)} ~ \underline{Description}")

  outStr = fig_t.format(tikzpic=tikzpic,matrix=mat,shortcap=scap,caption=cap,label=l,scale=s)
  
  with open(outp,'w') as fh:
    fh.write(outStr)


  
if __name__ == "__main__":
  try:
    basedir = sys.argv[1]
  except:
    basedir = ".."
  main(basedir)
