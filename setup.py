#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='codestyle',
    version='0.0.26',
    author=u'Sergey Levitin',
    author_email='selevit@gmail.com',
    packages=find_packages(),
    package_data={
        'codestyle': ['standards/*'],
    },
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/webpp-studio/codestyle',
    license='GPL licence, see LICENCE',
    description='Extendable codestyle checker and fixer',
    long_description=open('README.rst').read(),
    scripts=['scripts/codestyle'],
    install_requires=['pep8', 'autopep8', 'flake8', 'autoflake'],
    test_suite='tests'
)
