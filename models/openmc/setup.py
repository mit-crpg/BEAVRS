__author__ = 'Nicholas Horelik'
__email__ = 'nhorelik@mit.edu'

from distutils.core import setup

setup(name='BEAVRS',
      version='0.2',
      description='A package for building the BEAVRS PWR model',
      author=__author__,
      author_email=__email__,
      packages=['beavrs'],
      package_data = {'beavrs': ['*.txt']},
      )
