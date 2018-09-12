#!/usr/bin/env python

import os
from beavrs.builder import BEAVRS
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
(options, args) = p.parse_args()

if not len(args) == 0:
    p.print_help()

b = BEAVRS(is_symmetric=options.is_symmetric, is_2d=options.is_2d)
b.write_openmc_geometry()
b.write_openmc_materials()
b.write_openmc_plots()
b.write_openmc_settings()

