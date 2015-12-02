#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    readme_text = file('README.rst', 'rb').read()
except IOError,e:
    readme_text = ''

setup(name = "airwing_autopublish",
    version = "1.0.0",
    description = "GeoServer REST Configuration",
    long_description = readme_text,
    keywords = "GeoServer REST Configuration",
    license = "MIT",
    url = "https://github.com/surongxiang/gsconfig",
    author = "wushi",
    author_email = "hfutsrx@gmail.com",
    install_requires = [
        'httplib2>=0.7.4',
        'gisdata==0.5.4'
    ],
    package_dir = {'':'src'},
    packages = find_packages('src'),
    test_suite = "test.catalogtests",
    classifiers = [
                 'Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Scientific/Engineering :: GIS',
                ]
)

