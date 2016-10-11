#!/usr/bin/env python

import os
from setuptools import setup

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
# read the docs could not compile numpy and c extensions
if on_rtd:
    setup_requires = []
    install_requires = []
else:
    setup_requires = [
        'nose',
        'coverage',
        'scikit-learn',
    ]
    install_requires = [
        'six',
        'numpy',
        'scipy',
        'matplotlib',
    ]

setup(
    name='striatum',
    version='0.1.1',
    description='Contextual bandit in python',
    long_description='Contextual bandit in python',
    author='Y.-Y. Yang, Y.-A. Lin',
    author_email='b01902066@csie.ntu.edu.tw, r02922163@csie.ntu.edu.tw',
    url='https://github.com/ntucllab/striatum',
    setup_requires=setup_requires,
    install_requires=install_requires,
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    test_suite='nose.collector',
    packages=[
        'striatum',
        'striatum.bandit',
        'striatum.storage'
    ],
    package_dir={
        'striatum': 'striatum',
        'striatum.bandit': 'striatum/bandit',
        'striatum.storage': 'striatum/storage'
    },
)
