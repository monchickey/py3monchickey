#!/usr/bin/env python3
# coding=utf-8
import os
import sys
import codecs

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ['monchickey']

requires = [
    'PyMySQL>=0.7.11',
    'pyyaml>=3.11',
    'xxhash>=1.2.0'
]

longdesc = '''
This is a tool library based on python 3. It is called monchickey.
Features include file handling, database connection acquisition, 
Network communication and simple system command calls, 
The most commonly used for data calculation, filtering and conversion.

Required packages:
    PyMySQL
    PyYAML
    xxhash
'''

about = {}
with codecs.open(os.path.join(here, 'monchickey', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=longdesc,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    license=about['__license__'],
    python_requires=">= 3.5",
    # platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
