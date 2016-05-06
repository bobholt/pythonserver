# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pythonserver',
    version='0.0.1',
    description='Basic Python Server for Flask Applications',
    long_description=readme,
    author='Bob Holt',
    author_email='bobholt@gmail.com',
    url='http://bobholt.me',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
