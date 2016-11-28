# Actual setup tools
from setuptools import setup, find_packages

import os

here = os.path.abspath(path.dirname(__file__))

setup(
    name='LibModule',
    version='1.0.0',

    description='A python library',
    long_description="".join([line for line in '''
    This is a python library.
    '''.strip().split("\n") if len(line) > 0]),
    classifiers=[
        'Bad Cls :: Do not publish :: 3.5',
    ],

    keywords='lib test',

    packages=find_packages(),
)