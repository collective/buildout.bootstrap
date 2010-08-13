import os
from setuptools import setup, find_packages

description = """A zc.buildout extension that adds a zc.buildout bootstrap.py
    file to your buildout."""


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='buildout.bootstrap',
    version='1.1',
    description=description,
    long_description=read('README.txt') + read('docs/HISTORY.txt'),
    packages=find_packages(),
    install_requires=['setuptools'],
    namespace_packages=['buildout'],
    entry_points={
        "zc.buildout.extension": ["default = buildout.bootstrap:install"]})
