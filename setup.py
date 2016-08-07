#!/usr/bin/env/python

from distutils.core import setup
setup(name='rhost',
      version='1.0',
      author='Andrew Patterson',
      author_email='andrew.patterson@hp.com',
      maintainer='Andrew Patterson',
      maintainer_email='andrew.patterson@hp.com',
      url='https://github.hpe.com/andrew-patterson/apwot-storage-tests',
      description="Andrew Patterson's Wacked-Out (apwot) storage tests",
      long_description="""Andrew Patterson's Wacked-Out storage tests (apwot) collection.

A collection of python storage tests. Unsupported, so use
at your own risk.""",
      download_url='',
      license='Proprietary',
      packages=['rhost'],
      package_dir={'rhost': 'rhost/lib'},
      scripts=['rhost/bin/rhost',],
      )
