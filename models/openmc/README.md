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
and a Jupyter notebook `extract-assm.ipynb` to extract a single assembly of BEAVRS.

