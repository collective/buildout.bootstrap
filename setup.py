# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='buildout.bootstrap',
    version='1.2',
    description="""A zc.buildout extension that adds a (zc.buildout) bootstrap.py
    file to your buildout.""",
    long_description=(read('README.txt') + read('docs/INSTALL.txt') +
        read('docs/HISTORY.txt') +
        read('docs/CONTRIBUTORS.txt')),
    keywords='buildout bootstrap',
    author='Alex Clark',
    author_email='aclark@aclark.net',
    url='http://svn.plone.org/svn/collective/buildout/buildout.bootstrap',
    license='ZPL',
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
        ],
    packages=find_packages(),
    install_requires=['distribute'],
    namespace_packages=['buildout'],
    entry_points={
        "zc.buildout.extension": ["default = buildout.bootstrap:install"]})
