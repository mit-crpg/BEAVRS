#!/usr/bin/env python

import os
from beavrs.builder import BEAVRS

try:
    os.mkdir('build')
except OSError: pass
os.chdir('build')

b = BEAVRS()
b.write_openmc_geometry()
b.write_openmc_materials()
b.write_openmc_plots()
b.write_openmc_settings()

