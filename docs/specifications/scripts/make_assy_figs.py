#!/usr/bin/env python

import sys
import os

try:
  base = sys.argv[1]
except:
  base = ".."

seq = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']

node_t = "\\renewcommand{{\Node{0}{1}}}{{{text}}}\n"
node_link_t = "\\renewcommand{{\NodeLink{0}{1}}}{{{link}}}\n"
node_fill_t = "\\renewcommand{{\NodeFill{0}{1}}}{{{fill}}}\n"

fig_str = r"""\begin{{figure}}[htpb]
  \centering
  \hypertarget{{{label}_target}}{{}}
  \begin{{tikzpicture}}[draw=black, x=\Size,y=\Size, scale={scale}]
      \foreach \col/\colLetter in \Sequence {{%
          \foreach \row/\rowLetter in \Sequence{{%
              \pgfmathtruncatemacro{{\value}}{{\col+\NumOfColumns*(\row-1)}}
              \def\NodeText{{\expandafter\csname Node\rowLetter\colLetter\endcsname}}
              \def\NodeLink{{\expandafter\csname NodeLink\rowLetter\colLetter\endcsname}}
              \def\NodeFill{{\expandafter\csname NodeFill\rowLetter\colLetter\endcsname}}
              \node [Square, hyperlink node=\NodeLink, fill=\NodeFill] at ($(\col,-\row)-(0.5,0.5)$) {{\NodeText}};
          }}
      }}
{extra}
  \end{{tikzpicture}}
  \caption[{altcap}]{{{caption} Source: {source} \label{{{label}}}}}
\end{{figure}}"""

GTU = ("G","fig_guidetube_pin","yellow!40")
INS = ("I","fig_instr_pin","white")
BA = ("B","fig_ba_pin","red!40")
default = ("","fig_fuel_pin","blue!10")

    
################################################################################
################################################################################
################################################################################

# Cycle 1

######################## 6 BA assembly

outp = os.path.join(base,"specifications{0}assy{0}figs{0}6ba.tex".format(os.sep))

outStr = ""
for r,R in enumerate(seq):
  for c,C in enumerate(seq):
    node = default

    # Guide tube positions
    if r+1 == 4 and c+1 == 4: node = BA
    if r+1 == 3 and c+1 == 6: node = BA
    if r+1 == 3 and c+1 == 9: node = GTU
    if r+1 == 3 and c+1 == 12: node = BA
    if r+1 == 4 and c+1 == 14: node = BA
    
    if r+1 == 6 and c+1 == 3: node = BA
    if r+1 == 6 and c+1 == 6: node = GTU
    if r+1 == 6 and c+1 == 9: node = GTU
    if r+1 == 6 and c+1 == 12: node = GTU
    if r+1 == 6 and c+1 == 15: node = BA
    
    if r+1 == 9 and c+1 == 3: node = GTU
    if r+1 == 9 and c+1 == 6: node = GTU
    if r+1 == 9 and c+1 == 9: node = INS
    if r+1 == 9 and c+1 == 12: node = GTU
    if r+1 == 9 and c+1 == 15: node = GTU
    
    if r+1 == 12 and c+1 == 3: node = GTU
    if r+1 == 12 and c+1 == 6: node = GTU
    if r+1 == 12 and c+1 == 9: node = GTU
    if r+1 == 12 and c+1 == 12: node = GTU
    if r+1 == 12 and c+1 == 15: node = GTU
    
    if r+1 == 14 and c+1 == 4: node = GTU
    if r+1 == 15 and c+1 == 6: node = GTU
    if r+1 == 15 and c+1 == 9: node = GTU
    if r+1 == 15 and c+1 == 12: node = GTU
    if r+1 == 14 and c+1 == 14: node = GTU
    
    outStr += node_t.format(R,C,text=node[0])
    outStr += node_link_t.format(R,C,link=node[1])
    outStr += node_fill_t.format(R,C,fill=node[2])

e = "      \\draw[->,thick] (8.5,-1) -- (8.5,0);\n      \\node[anchor=south] at (8.5,0) {Core Center};"

outStr += fig_str.format(extra=e,scale=1,altcap="The 6BA burnable absorber configuration.",caption="The 6BA burnable absorber configuration. Blank locations denote fuel rods, \\textbf{G} denotes a guide tube location, \\textbf{B} denotes a burnable absorber rod, and \\textbf{I} denotes a guide tube position that might contain an instrument tube.",label="ass_6ba",
                         source=r"\ref{num:sheet_BPs}")
                         
with open(outp,'w') as fh:
  fh.write(outStr)

######################## 12 BA assembly

outp = os.path.join(base,"specifications{0}assy{0}figs{0}12ba.tex".format(os.sep))

outStr = ""
for r,R in enumerate(seq):
  for c,C in enumerate(seq):
    node = default

    # Guide tube positions
    if r+1 == 4 and c+1 == 4: node = BA
    if r+1 == 3 and c+1 == 6: node = BA
    if r+1 == 3 and c+1 == 9: node = GTU
    if r+1 == 3 and c+1 == 12: node = BA
    if r+1 == 4 and c+1 == 14: node = BA
    
    if r+1 == 6 and c+1 == 3: node = BA
    if r+1 == 6 and c+1 == 6: node = GTU
    if r+1 == 6 and c+1 == 9: node = GTU
    if r+1 == 6 and c+1 == 12: node = GTU
    if r+1 == 6 and c+1 == 15: node = BA
    
    if r+1 == 9 and c+1 == 3: node = GTU
    if r+1 == 9 and c+1 == 6: node = GTU
    if r+1 == 9 and c+1 == 9: node = INS
    if r+1 == 9 and c+1 == 12: node = GTU
    if r+1 == 9 and c+1 == 15: node = GTU
    
    if r+1 == 12 and c+1 == 3: node = BA
    if r+1 == 12 and c+1 == 6: node = GTU
    if r+1 == 12 and c+1 == 9: node = GTU
    if r+1 == 12 and c+1 == 12: node = GTU
    if r+1 == 12 and c+1 == 15: node = BA
    
    if r+1 == 14 and c+1 == 4: node = BA
    if r+1 == 15 and c+1 == 6: node = BA
    if r+1 == 15 and c+1 == 9: node = GTU
    if r+1 == 15 and c+1 == 12: node = BA
    if r+1 == 14 and c+1 == 14: node = BA
    
    outStr += node_t.format(R,C,text=node[0])
    outStr += node_link_t.format(R,C,link=node[1])
    outStr += node_fill_t.format(R,C,fill=node[2])
    
outStr += fig_str.format(extra="",scale=1,altcap="The 12BA burnable absorber configuration for cycle 1.",caption="The 12BA burnable absorber configuration for cycle 1. Blank locations denote fuel rods, \\textbf{G} denotes a guide tube location, \\textbf{B} denotes a burnable absorber rod, and \\textbf{I} denotes a guide tube position that might contain an instrument tube.",label="ass_12ba",
                         source=r"\ref{num:sheet_BPs}")
                         
with open(outp,'w') as fh:
  fh.write(outStr)

######################## 15 BA assembly

outp = os.path.join(base,"specifications{0}assy{0}figs{0}15ba.tex".format(os.sep))

outStr = ""
for r,R in enumerate(seq):
  for c,C in enumerate(seq):
    node = default

    # Guide tube positions
    if r+1 == 4 and c+1 == 4: node = BA
    if r+1 == 3 and c+1 == 6: node = BA
    if r+1 == 3 and c+1 == 9: node = BA
    if r+1 == 3 and c+1 == 12: node = BA
    if r+1 == 4 and c+1 == 14: node = GTU
    
    if r+1 == 6 and c+1 == 3: node = BA
    if r+1 == 6 and c+1 == 6: node = BA
    if r+1 == 6 and c+1 == 9: node = BA
    if r+1 == 6 and c+1 == 12: node = BA
    if r+1 == 6 and c+1 == 15: node = GTU
    
    if r+1 == 9 and c+1 == 3: node = BA
    if r+1 == 9 and c+1 == 6: node = BA
    if r+1 == 9 and c+1 == 9: node = INS
    if r+1 == 9 and c+1 == 12: node = BA
    if r+1 == 9 and c+1 == 15: node = GTU
    
    if r+1 == 12 and c+1 == 3: node = BA
    if r+1 == 12 and c+1 == 6: node = BA
    if r+1 == 12 and c+1 == 9: node = BA
    if r+1 == 12 and c+1 == 12: node = BA
    if r+1 == 12 and c+1 == 15: node = GTU
    
    if r+1 == 14 and c+1 == 4: node = GTU
    if r+1 == 15 and c+1 == 6: node = GTU
    if r+1 == 15 and c+1 == 9: node = GTU
    if r+1 == 15 and c+1 == 12: node = GTU
    if r+1 == 14 and c+1 == 14: node = GTU
    
    outStr += node_t.format(R,C,text=node[0])
    outStr += node_link_t.format(R,C,link=node[1])
    outStr += node_fill_t.format(R,C,fill=node[2])

e = "      \\draw[->,thick] (0,-1) -- (-1,0);\n      \\node[anchor=south] at (-1,0) {Core Center};"
    
outStr += fig_str.format(extra=e,scale=1,altcap="The 15BA burnable absorber configuration.",caption="The 15BA burnable absorber configuration. Blank locations denote fuel rods, \\textbf{G} denotes a guide tube location, \\textbf{B} denotes a burnable absorber rod, and \\textbf{I} denotes a guide tube position that might contain an instrument tube.",label="ass_15ba",
                         source=r"\ref{num:sheet_BPs}")
                         
with open(outp,'w') as fh:
  fh.write(outStr)

######################## 16 BA assembly

outp = os.path.join(base,"specifications{0}assy{0}figs{0}16ba.tex".format(os.sep))

outStr = ""
for r,R in enumerate(seq):
  for c,C in enumerate(seq):
    node = default

    # Guide tube positions
    if r+1 == 4 and c+1 == 4: node = BA
    if r+1 == 3 and c+1 == 6: node = BA
    if r+1 == 3 and c+1 == 9: node = BA
    if r+1 == 3 and c+1 == 12: node = BA
    if r+1 == 4 and c+1 == 14: node = BA
    
    if r+1 == 6 and c+1 == 3: node = BA
    if r+1 == 6 and c+1 == 6: node = GTU
    if r+1 == 6 and c+1 == 9: node = GTU
    if r+1 == 6 and c+1 == 12: node = GTU
    if r+1 == 6 and c+1 == 15: node = BA
    
    if r+1 == 9 and c+1 == 3: node = BA
    if r+1 == 9 and c+1 == 6: node = GTU
    if r+1 == 9 and c+1 == 9: node = INS
    if r+1 == 9 and c+1 == 12: node = GTU
    if r+1 == 9 and c+1 == 15: node = BA
    
    if r+1 == 12 and c+1 == 3: node = BA
    if r+1 == 12 and c+1 == 6: node = GTU
    if r+1 == 12 and c+1 == 9: node = GTU
    if r+1 == 12 and c+1 == 12: node = GTU
    if r+1 == 12 and c+1 == 15: node = BA
    
    if r+1 == 14 and c+1 == 4: node = BA
    if r+1 == 15 and c+1 == 6: node = BA
    if r+1 == 15 and c+1 == 9: node = BA
    if r+1 == 15 and c+1 == 12: node = BA
    if r+1 == 14 and c+1 == 14: node = BA
    
    outStr += node_t.format(R,C,text=node[0])
    outStr += node_link_t.format(R,C,link=node[1])
    outStr += node_fill_t.format(R,C,fill=node[2])
    
outStr += fig_str.format(extra="",scale=1,altcap="The 16BA burnable absorber configuration.",caption="The 16BA burnable absorber configuration. Blank locations denote fuel rods, \\textbf{G} denotes a guide tube location, \\textbf{B} denotes a burnable absorber rod, and \\textbf{I} denotes a guide tube position that might contain an instrument tube.",label="ass_16ba",
                         source=r"\ref{num:sheet_BPs}")
                         
with open(outp,'w') as fh:
  fh.write(outStr)

######################## 20 BA assembly

outp = os.path.join(base,"specifications{0}assy{0}figs{0}20ba.tex".format(os.sep))

outStr = ""
for r,R in enumerate(seq):
  for c,C in enumerate(seq):
    node = default

    # Guide tube positions
    if r+1 == 4 and c+1 == 4: node = BA
    if r+1 == 3 and c+1 == 6: node = BA
    if r+1 == 3 and c+1 == 9: node = BA
    if r+1 == 3 and c+1 == 12: node = BA
    if r+1 == 4 and c+1 == 14: node = BA
    
    if r+1 == 6 and c+1 == 3: node = BA
    if r+1 == 6 and c+1 == 6: node = BA
    if r+1 == 6 and c+1 == 9: node = GTU
    if r+1 == 6 and c+1 == 12: node = BA
    if r+1 == 6 and c+1 == 15: node = BA
    
    if r+1 == 9 and c+1 == 3: node = BA
    if r+1 == 9 and c+1 == 6: node = GTU
    if r+1 == 9 and c+1 == 9: node = INS
    if r+1 == 9 and c+1 == 12: node = GTU
    if r+1 == 9 and c+1 == 15: node = BA
    
    if r+1 == 12 and c+1 == 3: node = BA
    if r+1 == 12 and c+1 == 6: node = BA
    if r+1 == 12 and c+1 == 9: node = GTU
    if r+1 == 12 and c+1 == 12: node = BA
    if r+1 == 12 and c+1 == 15: node = BA
    
    if r+1 == 14 and c+1 == 4: node = BA
    if r+1 == 15 and c+1 == 6: node = BA
    if r+1 == 15 and c+1 == 9: node = BA
    if r+1 == 15 and c+1 == 12: node = BA
    if r+1 == 14 and c+1 == 14: node = BA
    
    outStr += node_t.format(R,C,text=node[0])
    outStr += node_link_t.format(R,C,link=node[1])
    outStr += node_fill_t.format(R,C,fill=node[2])
    
outStr += fig_str.format(extra="",scale=1,altcap="The 20BA burnable absorber configuration.",caption="The 20BA burnable absorber configuration. Blank locations denote fuel rods, \\textbf{G} denotes a guide tube location, \\textbf{B} denotes a burnable absorber rod, and \\textbf{I} denotes a guide tube position that might contain an instrument tube.",label="ass_20ba",
                         source=r"\ref{num:sheet_BPs}")
                         
with open(outp,'w') as fh:
  fh.write(outStr)
  
################################################################################
################################################################################
################################################################################

# Cycle 2

######################## 4 BA assembly
nba = 4
outp = os.path.join(base,"specifications{0}assy{0}figs{0}{1}ba.tex".format(os.sep,nba))

outStr = ""
for r,R in enumerate(seq):
  for c,C in enumerate(seq):
    node = default

    # Guide tube positions
    if r+1 == 4 and c+1 == 4: node = BA
    if r+1 == 3 and c+1 == 6: node = GTU
    if r+1 == 3 and c+1 == 9: node = GTU
    if r+1 == 3 and c+1 == 12: node = GTU
    if r+1 == 4 and c+1 == 14: node = BA
    
    if r+1 == 6 and c+1 == 3: node = GTU
    if r+1 == 6 and c+1 == 6: node = GTU
    if r+1 == 6 and c+1 == 9: node = GTU
    if r+1 == 6 and c+1 == 12: node = GTU
    if r+1 == 6 and c+1 == 15: node = GTU
    
    if r+1 == 9 and c+1 == 3: node = GTU
    if r+1 == 9 and c+1 == 6: node = GTU
    if r+1 == 9 and c+1 == 9: node = INS
    if r+1 == 9 and c+1 == 12: node = GTU
    if r+1 == 9 and c+1 == 15: node = GTU
    
    if r+1 == 12 and c+1 == 3: node = GTU
    if r+1 == 12 and c+1 == 6: node = GTU
    if r+1 == 12 and c+1 == 9: node = GTU
    if r+1 == 12 and c+1 == 12: node = GTU
    if r+1 == 12 and c+1 == 15: node = GTU
    
    if r+1 == 14 and c+1 == 4: node = BA
    if r+1 == 15 and c+1 == 6: node = GTU
    if r+1 == 15 and c+1 == 9: node = GTU
    if r+1 == 15 and c+1 == 12: node = GTU
    if r+1 == 14 and c+1 == 14: node = BA
    
    outStr += node_t.format(R,C,text=node[0])
    outStr += node_link_t.format(R,C,link=node[1])
    outStr += node_fill_t.format(R,C,fill=node[2])
    
outStr += fig_str.format(extra="",scale=1,altcap="The {0}BA burnable absorber configuration.".format(nba),caption="The {0}BA burnable absorber configuration. Blank locations denote fuel rods, \\textbf{{G}} denotes a guide tube location, \\textbf{{B}} denotes a burnable absorber rod, and \\textbf{{I}} denotes a guide tube position that might contain an instrument tube.".format(nba),label="ass_{0}ba".format(nba),
                         source=r"\ref{num:sheet_BPs}")
                         
with open(outp,'w') as fh:
  fh.write(outStr)

######################## 8 BA assembly
nba = 8
outp = os.path.join(base,"specifications{0}assy{0}figs{0}{1}ba.tex".format(os.sep,nba))

outStr = ""
for r,R in enumerate(seq):
  for c,C in enumerate(seq):
    node = default

    # Guide tube positions
    if r+1 == 4 and c+1 == 4: node = BA
    if r+1 == 3 and c+1 == 6: node = GTU
    if r+1 == 3 and c+1 == 9: node = GTU
    if r+1 == 3 and c+1 == 12: node = GTU
    if r+1 == 4 and c+1 == 14: node = BA
    
    if r+1 == 6 and c+1 == 3: node = GTU
    if r+1 == 6 and c+1 == 6: node = GTU
    if r+1 == 6 and c+1 == 9: node = BA
    if r+1 == 6 and c+1 == 12: node = GTU
    if r+1 == 6 and c+1 == 15: node = GTU
    
    if r+1 == 9 and c+1 == 3: node = GTU
    if r+1 == 9 and c+1 == 6: node = BA
    if r+1 == 9 and c+1 == 9: node = INS
    if r+1 == 9 and c+1 == 12: node = BA
    if r+1 == 9 and c+1 == 15: node = GTU
    
    if r+1 == 12 and c+1 == 3: node = GTU
    if r+1 == 12 and c+1 == 6: node = GTU
    if r+1 == 12 and c+1 == 9: node = BA
    if r+1 == 12 and c+1 == 12: node = GTU
    if r+1 == 12 and c+1 == 15: node = GTU
    
    if r+1 == 14 and c+1 == 4: node = BA
    if r+1 == 15 and c+1 == 6: node = GTU
    if r+1 == 15 and c+1 == 9: node = GTU
    if r+1 == 15 and c+1 == 12: node = GTU
    if r+1 == 14 and c+1 == 14: node = BA
    
    outStr += node_t.format(R,C,text=node[0])
    outStr += node_link_t.format(R,C,link=node[1])
    outStr += node_fill_t.format(R,C,fill=node[2])
    
outStr += fig_str.format(extra="",scale=1,altcap="The {0}BA burnable absorber configuration.".format(nba),caption="The {0}BA burnable absorber configuration. Blank locations denote fuel rods, \\textbf{{G}} denotes a guide tube location, \\textbf{{B}} denotes a burnable absorber rod, and \\textbf{{I}} denotes a guide tube position that might contain an instrument tube.".format(nba),label="ass_{0}ba".format(nba),
                         source=r"\ref{num:sheet_BPs}")
                         
with open(outp,'w') as fh:
  fh.write(outStr)

######################## 12 BA assembly
nba = 12
outp = os.path.join(base,"specifications{0}assy{0}figs{0}{1}ba_c2.tex".format(os.sep,nba))

outStr = ""
for r,R in enumerate(seq):
  for c,C in enumerate(seq):
    node = default

    # Guide tube positions
    if r+1 == 4 and c+1 == 4: node = GTU
    if r+1 == 3 and c+1 == 6: node = BA
    if r+1 == 3 and c+1 == 9: node = GTU
    if r+1 == 3 and c+1 == 12: node = BA
    if r+1 == 4 and c+1 == 14: node = GTU
    
    if r+1 == 6 and c+1 == 3: node = BA
    if r+1 == 6 and c+1 == 6: node = GTU
    if r+1 == 6 and c+1 == 9: node = BA
    if r+1 == 6 and c+1 == 12: node = GTU
    if r+1 == 6 and c+1 == 15: node = BA
    
    if r+1 == 9 and c+1 == 3: node = GTU
    if r+1 == 9 and c+1 == 6: node = BA
    if r+1 == 9 and c+1 == 9: node = INS
    if r+1 == 9 and c+1 == 12: node = BA
    if r+1 == 9 and c+1 == 15: node = GTU
    
    if r+1 == 12 and c+1 == 3: node = BA
    if r+1 == 12 and c+1 == 6: node = GTU
    if r+1 == 12 and c+1 == 9: node = BA
    if r+1 == 12 and c+1 == 12: node = GTU
    if r+1 == 12 and c+1 == 15: node = BA
    
    if r+1 == 14 and c+1 == 4: node = GTU
    if r+1 == 15 and c+1 == 6: node = BA
    if r+1 == 15 and c+1 == 9: node = GTU
    if r+1 == 15 and c+1 == 12: node = BA
    if r+1 == 14 and c+1 == 14: node = GTU
    
    outStr += node_t.format(R,C,text=node[0])
    outStr += node_link_t.format(R,C,link=node[1])
    outStr += node_fill_t.format(R,C,fill=node[2])
    
outStr += fig_str.format(extra="",scale=1,altcap="The {0}BA burnable absorber configuration for cycle 2.".format(nba),caption="The {0}BA burnable absorber configuration for cycle 2. Blank locations denote fuel rods, \\textbf{{G}} denotes a guide tube location, \\textbf{{B}} denotes a burnable absorber rod, and \\textbf{{I}} denotes a guide tube position that might contain an instrument tube.".format(nba),label="ass_{0}ba_c2".format(nba),
                         source=r"\ref{num:sheet_BPs}")
                         
with open(outp,'w') as fh:
  fh.write(outStr)

