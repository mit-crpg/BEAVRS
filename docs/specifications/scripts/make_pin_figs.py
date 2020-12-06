#!/usr/bin/env python

from __future__ import division

import sys
import os

from math import pi, cos, sin

def main(base):

  r = r"\ref{{{0}}}"
#  m = r.format("num:missing")


  a = r.format("num:assumed_thimble")
  f = r.format("num:sheet_FL")

  makepin([0.56134, 0.60198],
          ['Water','Zircaloy'],
          ['mat_water','mat_zirc'],
          [r.format("num:GTIRrad"),r.format("num:GTORrad")],
          "Empty guide tube pin geometry above the dashpot.",
          "fig_guidetube_pin",
          6,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_guidetube.tex".format(os.sep)),
          0.65)

  makepin([0.50419, 0.54610],
          ['Water','Zircaloy'],
          ['mat_water','mat_zirc'],
          [r.format("num:GTDPIRrad"),r.format("num:GTDPORrad")],
          "Empty guide tube pin geometry at the dashpot.",
          "fig_guidetube_da_pin",
          6,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_guidetube_da.tex".format(os.sep)),
          0.65)

  makepin([0.39218, 0.40005, 0.45720],
          ['Fuel','Helium','Zircaloy'],
          ['mat_fuel16','mat_helium','mat_zirc'],
          [r.format("num:fuelpellrad"),r.format("num:fuelIRrad"),r.format("num:fuelORrad")],
          "Fuel pin geometry.",
          "fig_fuel_pin",
          8,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_fuel.tex".format(os.sep)),
          0.65)

  makepin([0.06459, 0.40005, 0.45720],
          ['Inconel','Helium','Zircaloy'],
          ['mat_inconel','mat_helium','mat_zirc'],
          [r.format("num:plenum_spring"),r.format("num:fuelIRrad"),r.format("num:fuelORrad")],
          "Upper fuel pin plenum geometry.",
          "fig_fuel_pin_plenum",
          8,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_fuel_plenum.tex".format(os.sep)),
          0.65)

  makepin([0.38227,0.38608, 0.48387, 0.56134, 0.60198],
          ['Ag-In-Cd','Helium','SS304','Water','Zircaloy'],
          ['mat_aic_rod','mat_helium','mat_SS304','mat_water','mat_zirc'],
          [r.format("num:CRaicOR"), r.format("num:CRthimIR"),r.format("num:CRthimOR"),r.format("num:GTIRrad"),r.format("num:GTORrad")],
          "Control rod pin lower region geometry.",
          "fig_cr_pin",
          6,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_cr.tex".format(os.sep)),
          0.5)

  makepin([0.37338,0.38608, 0.48387, 0.56134, 0.60198],
          ['B4C','Helium','SS304','Water','Zircaloy'],
          ['mat_b4c_rod','mat_helium','mat_SS304','mat_water','mat_zirc'],
          [r.format("num:CRb4cOR"),r.format("num:CRthimIR"),r.format("num:CRthimOR"),r.format("num:GTIRrad"),r.format("num:GTORrad")],
          "Control rod pin upper region geometry.",
          "fig_cr_pin_upper",
          6,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_cr_upper.tex".format(os.sep)),
          0.5)

  makepin([0.06459,0.38608, 0.48387, 0.56134, 0.60198],
          ['Inconel','Helium','SS304','Water','Zircaloy'],
          ['mat_inconel','mat_helium','mat_SS304','mat_water','mat_zirc'],
          [r.format("num:cr_plenum_spring"),r.format("num:CRthimIR"),r.format("num:CRthimOR"),r.format("num:GTIRrad"),r.format("num:GTORrad")],
          "Control rod pin plenum geometry.",
          "fig_cr_pin_plenum",
          6,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_cr_plenum.tex".format(os.sep)),
          0.75)

  makepin([0.37845,0.38608, 0.48387, 0.56134, 0.60198],
          ['SS304','Helium','SS304','Water','Zircaloy'],
          ['mat_SS304','mat_helium','mat_SS304','mat_water','mat_zirc'],
          [r.format("num:CRspacerOR"),r.format("num:CRthimIR"),r.format("num:CRthimOR"),r.format("num:GTIRrad"),r.format("num:GTORrad")],
          "Control rod pin spacer geometry.",
          "fig_cr_pin_spacer",
          6,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_cr_spacer.tex".format(os.sep)),
          0.5)

  makepin([0.21400, 0.23051, 0.24130, 0.42672, 0.43688, 0.48387, 0.56134, 0.60198],
          ['Air','SS304','Helium','Borosilicate Glass','Helium','SS304','Water','Zircaloy'],
          ['mat_air','mat_SS304','mat_helium','mat_borosilicate','mat_helium','mat_SS304','mat_water','mat_zirc'],
          [r.format("num:BPinnercladIR"),r.format("num:BPinnercladOR"),r.format("num:BPpoisonIR"),r.format("num:BPpoisonOR"),r.format("num:BPoutercladIR"),r.format("num:BPoutercladOR"),r.format("num:GTIRrad"),r.format("num:GTORrad")],
          "Burnable absorber pin geometry above the dashpot.",
          "fig_ba_pin",
          8,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_ba.tex".format(os.sep)),
          0.65)

  makepin([0.21400, 0.23051, 0.43688, 0.48387, 0.56134, 0.60198],
          ['Air','SS304','Helium','SS304','Water','Zircaloy'],
          ['mat_air','mat_SS304','mat_helium','mat_SS304','mat_water','mat_zirc'],
          [r.format("num:BPinnercladIR"),r.format("num:BPinnercladOR"),r.format("num:BPoutercladIR"),r.format("num:BPoutercladOR"),r.format("num:GTIRrad"),r.format("num:GTORrad")],
          "Burnable absorber pin plenum geometry",
          "fig_ba_pin_plenum",
          8,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_ba_plenum.tex".format(os.sep)),
          0.65)

  makepin([0.436880, 0.483870, 0.56134, 0.60198],
          ['Air','Zircaloy','Water','Zircaloy'],
          ['mat_air','mat_zirc','mat_water','mat_zirc'],
          [r.format("num:ITthimIR"),r.format("num:ITthimOR"),r.format("num:GTIRrad"),r.format("num:GTORrad")],
          "Instrument tube pin geometry (both above and at the dashpot).",
          "fig_instr_pin",
          6,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_instr.tex".format(os.sep)),
          0.65)

  makepin([0.436880, 0.483870],
          ['Air','Zircaloy'],
          ['mat_air','mat_zirc'],
          [r.format("num:ITthimIR"),r.format("num:ITthimOR")],
          "Bare instrument thimble (below fuel rod region).",
          "fig_instr_pin_bare",
          6,
          os.path.join(base,"specifications{0}pin{0}figs{0}tikz_instr_bare.tex".format(os.sep)),
          0.65)

def makepin(rs,ms,ls,ss,c,l,s,outp,pos):

  arc = pi/6
  theta = arc

  fig_t = r"""\begin{{tikzpicture}}[scale={scale},auto]
  {fig_mat}
      \end{{tikzpicture}}
      \begin{{tikzpicture}}
  {matrix}
\end{{tikzpicture}}"""

  circ_t = """      \draw (0,0) circle ({r});\n"""
  arrow_t = """      \draw[->] (0,0) -- node[pos={pos}] {{{label}}} ({x:.3},{y:.3});\n"""

  f = ""

  for i,r in enumerate(rs):
    f += circ_t.format(r=r)
    x = r*cos(pi/2 - theta)
    y = r*sin(pi/2 - theta)
    f += arrow_t.format(label=i+1,x=round(x,3),y=round(y,3),pos=pos)
    theta += arc

  mat_t=r"""     \matrix [matrix of nodes]
      {{
          Arrow & Radius (cm) & Material & \numrefheader \\{matrows}
      }};"""
  matrow_t = """\n        {0} & {1:0<7.5} & \\node[hyperlink node={3}]{{{2}}}; & {source}\\\ """
  rows = ""
  for i,(r,m,ref,sour) in enumerate(zip(rs,ms,ls,ss)):
    rows += matrow_t.format(i+1,r,m,ref,source=sour)

  outStr = fig_t.format(fig_mat=f, scale=s, caption=c,label=l, matrix=mat_t.format(matrows=rows))

  with open(outp,'w') as fh:
      fh.write(outStr)

if __name__ == "__main__":
  try:
    basedir = sys.argv[1]
  except:
    basedir = ".."
  main(basedir)
