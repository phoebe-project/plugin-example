from distutils.core import setup

name = 'pluginexample'
version = 'devel'
description = 'example of a PHOEBE 2.0 plugin'

setup(name=name,
      version=version,
      description=description,
      packages = [name])
