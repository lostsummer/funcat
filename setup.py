#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Hua Liang[Stupid ET] <et@everet.org>
#

from setuptools import (
    find_packages,
    setup,
)

from pip.req import parse_requirements


setup(
    name='funcat',
    version='0.0.1',
    description='funcat',
    packages=find_packages(exclude=[]),
    author='et@everet.org',
    author_email='et@everet.org',
    package_data={'': ['*.*']},
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    zip_safe=False,
)