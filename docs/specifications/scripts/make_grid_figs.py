#!/usr/bin/env python

from __future__ import division

import sys
import os

from math import pi, cos, sin, tan

def main(base):

  r = r"\ref{{{0}}}"
  m = r"\missing"
  f = r.format("num:sheet_FL")
  g = r.format("num:grid_spacer")
  
  makegrid( [0.39218, 0.40005, 0.45720, 0.61049, 0.629920],
            ['Fuel','Helium','Zircaloy','Water','Zircaloy'],
            ['mat_fuel16','mat_helium','mat_zirc','mat_water','mat_inconel'],
            [r.format("num:fuelpellrad"),r.format("num:fuelIRrad"),r.format("num:fuelORrad"),g,g],
            ['red','green!60!black','blue','magenta!80!black','orange!60!black'],
            "[Fuel pincell geometry for the intermediate grid spacer inner egg-crate]",
            "Fuel pincell geometry for the Zircaloy intermediate grid spacer inner egg-crate, chosen to have a thickness of 0.0194cm.  Source: \\ref{num:grid_spacer}",
            "fig_grid_pin_i",
            5,
            os.path.join(base,"specifications{0}assy{0}figs{0}tikz_grid_inter.tex".format(os.sep)))
 
  makegrid( [0.39218, 0.40005, 0.45720, 0.61015, 0.629920],
            ['Fuel','Helium','Zircaloy','Water','Inconel'],
            ['mat_fuel16','mat_helium','mat_zirc','mat_water','mat_inconel'],
            [r.format("num:fuelpellrad"),r.format("num:fuelIRrad"),r.format("num:fuelORrad"),g,g],
            ['red','green!60!black','blue','magenta!80!black','orange!60!black'],
            "[Fuel pincell geometry for the top/bottom grid spacer inner egg-crate]",
            "Fuel pincell geometry for the Inconel 718 top/bottom grid spacer inner egg-crate, chosen to have a thickness of 0.0198cm.  Source: \\ref{num:grid_spacer}",
            "fig_grid_pin_tb",
            5,
            os.path.join(base,"specifications{0}assy{0}figs{0}tikz_grid_tb.tex".format(os.sep)))

def makegrid(rs,ms,ls,ss,cols,sc,c,l,s,outp):

  arc = pi/6
  theta = arc

  fig_t = r"""\begin{{figure}}[htbp]

      \centering
      
      \begin{{tikzpicture}}[scale={scale},auto]
  {fig_mat}
      \end{{tikzpicture}}
      \begin{{tikzpicture}}
  {matrix}
      \end{{tikzpicture}}

      \caption{shortcap}{{ {caption} \label{{{label}}}}}
  \end{{figure}}"""

  circ_t = """      \draw (0,0) circle ({r});\n"""
  box_t = """      \draw (-{0},-{0}) rectangle ({0},{0}) ;\n"""
  arrow_t = """      \draw[->,thick,{color}] (0,0) -- node[pos={pos}] {{{label}}} ({x:.3},{y:.3});\n"""

  f = ""

  for i,r in enumerate(rs):
    if i < len(rs)-2:
      f += circ_t.format(r=r)
      x = r*cos(pi/2 - theta)
      y = r*sin(pi/2 - theta)
      f += arrow_t.format(label=i+1,x=round(x,3),y=round(y,3),pos=0.65,color=cols[i])
      theta += arc
    else:
      f += box_t.format(r)
      if i < len(rs)-1:
        x = 0.0
        y = -r
      else:
        x = -r
        y = 0.0
      f += arrow_t.format(label=i+1,x=round(x,3),y=round(y,3),pos=0.4,color=cols[i])
      theta += arc
      

  mat_t=r"""     \matrix [matrix of nodes]
      {{
          Arrow & Length (cm) & Material & \numrefheader\\{matrows}
      }};"""
  matrow_t = """\n        \\node[{color}]{{{0}}}; & \\node[{color}]{{{1:0<7.5}}}; & \\node[{color},hyperlink node={3}]{{{2}}}; & \\node[{color}]{{{source}}};\\\ """
  rows = ""
  for i,(r,m,ref,sour,color) in enumerate(zip(rs,ms,ls,ss,cols)):
    rows += matrow_t.format(i+1,r,m,ref,source=sour,color=color)

  outStr = fig_t.format(fig_mat=f, scale=s, shortcap=sc, caption=c, label=l,
                        matrix=mat_t.format(matrows=rows))

  with open(outp,'w') as fh:
      fh.write(outStr)

if __name__ == "__main__":
  try:
    basedir = sys.argv[1]
  except:
    basedir = ".."
  main(basedir)
