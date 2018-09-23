#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from skbuild import setup
from setuptools import find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "enum34==1.1.6",
    "six==1.11.0",
    "terminaltables==3.1.0",
]

setup_requirements = [
    "cmake",
    "pygccxml==1.9.1",
    "pyplusplus==1.8.1"
]

test_requirements = [ ]

setup(
    cmake_args=[
        '-DENABLE_COMPLX=OFF',
        '-DENABLE_AS2OBJ=OFF',
        '-DENABLE_LC3EDIT=OFF',
        '-DENABLE_LC3RUNNER=OFF',
        '-DENABLE_PYLC3=ON',
        '-DCMAKE_INSTALL_LIBDIR=pyLC3'
    ],
    cmake_source_dir='complx/',
    author="Zucchini Team",
    author_email='team@zucc.io',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python bindings for liblc3, the LC-3 emulator library behind complx.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyLC3',
    name='pyLC3',
    packages=find_packages(include=['pyLC3']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/zucchini/pyLC3',
    version='0.2.5',
    zip_safe=False,
)
