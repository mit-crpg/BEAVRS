#!/usr/bin/env python

import os
from beavrs.builder import BEAVRS
import beavrs.constants as c
from optparse import OptionParser

try:
    os.mkdir('build')
except OSError: pass
os.chdir('build')

usage = """usage: %prog [options]"""
p = OptionParser(usage=usage)
p.add_option('-d', '--2d', action='store_true', dest='is_2d',
             default=False, help='Create 2D BEAVRS input files,' \
             + ' 3D by default')
p.add_option('-s', '--symmetric', action='store_true', dest='is_symmetric',
             default=False, help='Create octant-symmetric input files,' \
             + ' not symmetric by default')
p.add_option('-z', '--rcca_d_z', dest='rcca_d_z',
             help='The number of steps withdrawn for RCC bank D, 0 by default',
             type=int, default=0)
(options, args) = p.parse_args()

if not len(args) == 0:
    p.print_help()

insertions = c.rcca_bank_steps_withdrawn_default
insertions['D'] = options.rcca_d_z

b = BEAVRS(is_symmetric=options.is_symmetric, is_2d=options.is_2d, rcca_z=insertions)
b.write_openmc_model()

