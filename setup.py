#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup for ipyatom."""

import io
from importlib import import_module
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
with open('test_requirements.txt') as f:
    test_requirements = f.read().splitlines()

with io.open('README.rst') as readme:
    setup(
        name='ipyatom',
        version=import_module('ipyatom').__version__,
        description='a package primarily for interfacing ase/pymatgen with ipyvolume/matplotlib',
        long_description=readme.read(),
        install_requires=requirements,
        tests_require=test_requirements,
        license='MIT',
        author='Chris Sewell',
        author_email='chrisj_sewell@hotmail.com',
        url='https://github.com/chrisjsewell/ipyatom',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Topic :: Scientific/Engineering :: Chemistry',
            'Topic :: Scientific/Engineering :: Physics',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
        ],
        keywords='python ase pymatgen ipyvolume atoms molecules visualisation',
        zip_safe=True,
        packages=find_packages(),
        package_data={'': ['*.csv']},
    )
