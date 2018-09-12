BEAVRS Input File Generator
===========================

The BEAVRS script has been developed to generate OpenMC input files. With
this script it should be much easier to extract single elements of the
geometry (e.g., single assemblies and pins) as well as make modifications to
different parts of the geometry.

This script is dependent on [OpenMC Python API](http://openmc.readthedocs.io/en/latest/pythonapi/index.html).

Installation
------------

This package can be installed with distutils via:

```bash
python setup.py install --user
```

Usage
-----

Once the module is installed, it can be constructed in python:

```python
from beavrs.builder import BEAVRS

model = BEAVRS()

model.write_openmc_geometry()
model.write_openmc_materials()
model.write_openmc_plots()
model.write_openmc_settings()

```

For convenience, also provided are a script `make_beavrs.py` to build the model
and Jupyter notebooks `extract-assm.ipynb` and `extract-pin.ipynb` to extract
single assemblies and pin cells of BEAVRS respectively.

For those looking to generate the input files for the 2D BEAVRS model and/or a model
that is symmetric in the x-y plane, the `-d` and `-s` flags can be used with the
`make_beavrs.py` script respectively. Details about these two models can be found
below:

2D BEAVRS Model
---------------

The 2D BEAVRS model is created from the 3D model by creating a bounding box around the
full core to restrict the problem to one assembly-width outside the outer-most assemblies
(i.e. 17 assemblies wide) in the x-y direction, and a 10cm slice in the z-direction.
The x-y surfaces have vacuum boundary conditions, while the 10cm slice is arbitrarily
chosen in a non-grid spacer region with reflective boundary conditions. The initial source
distribution is also updated accordingly.

Symmetric BEAVRS Model in x-y Plane
-----------------------------------

The only source of asymmetry in the x-y plane stems from the insertion of instrument tubes,
so the symmetric model replaces all instrument tubes with empty guide tubes, similar to all
other assemblies.
