#!/usr/bin/env python

import os
from beavrs.builder import BEAVRS
import beavrs.constants as c
from argparse import ArgumentParser

try:
    os.mkdir('build')
except OSError: pass
os.chdir('build')

p = ArgumentParser()
p.add_argument('-d', '--2d', action='store_true', dest='is_2d', default=False, \
               help='Create 2D BEAVRS input files 3D by default')
p.add_argument('-s', '--symmetric', action='store_true', dest='is_symmetric', \
               default=False, help='Create octant-symmetric input files,' \
               + ' not symmetric by default')
p.add_argument("--rcca-insertion", dest='rcca', nargs='*', default='', \
               help='RCCA insertion steps, provided as key-value pairs,' \
               + ' where even arguments are banks (keys) and odd arguments'
               + ' are insertion steps (values).' \
               + ' Valid keys are \'A\', \'B\', \'C\', \'D\', \'SA\',' \
               + ' \'SB\', \'SC\', \'SD\', and \'SE\'. Valid values are' \
               + ' integers between 0 and 228 (inclusive).')
args = p.parse_args()

insertions = c.rcca_bank_steps_withdrawn_default

# Error handle the RCCA insertion steps.
rcca_args = dict(zip(args.rcca[::2], args.rcca[1::2]))
for k in rcca_args:
  if k not in insertions.keys():
    raise Exception(f'{k} is not a valid RCCA bank! Valid options are \'A\',' + \
                    ' \'B\', \'C\', \'D\', \'SA\', \'SB\', \'SC\', \'SD\', and \'SE\'.')
  if rcca_args[k].isdigit() and (0 <= int(rcca_args[k]) and int(rcca_args[k]) <= 228):
     insertions[k] = int(rcca_args[k])
  else:
     raise Exception(f'Invalid RCCA insertion step {rcca_args[k]}! Valid insertion' \
                     + ' steps are integers between 0 and 228 (inclusive).')

b = BEAVRS(is_symmetric=args.is_symmetric, is_2d=args.is_2d, rcca_z=insertions)
b.write_openmc_model()

