#!/usr/bin/env python

import os

from setuptools import setup

module_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup(
        name='python_primer',
        version='2019.03.07',
        install_requires=["jupyter","matplotlib"],
        description='Repository for MSE 215 Python Primer',
        package_data={"resources.data.data_files": ["*.json"]},
        python_requires='>=3.6',
    )
