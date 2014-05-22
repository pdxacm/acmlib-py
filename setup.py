#!/usr/bin/env python2
#Copyright (C) 2014, Cameron Brandon White
# -*- coding: utf-8 -*-
import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='acmlib',
        version='0.1.1',
        description='library for the acm',
        author='Cameron Brandon White',
        author_email='cameronbwhite90@gmail.com',
        provides=[
            'acmlib',
        ],
        packages=[
            "acmlib",
        ],
        install_requires = [
            'characteristic',
            'requests',
        ],
        include_package_data=True,
    )
