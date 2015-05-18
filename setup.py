from setuptools import find_packages
from setuptools import setup
import os


VERSION = '1.4.7'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 2.7',
    ],
    description='Buildout extension to download ' + 
        'https://bootstrap.pypa.io/bootstrap-buildout.py ' +
        'automatically.',
    entry_points={
        "zc.buildout.extension": [
            "default = buildout.bootstrap:install"
        ]
    },
    install_requires=[
        'setuptools',
        'zc.buildout',
    ],
    keywords='buildout bootstrap',
    license='ZPL',
    long_description=(
        open('README.rst').read() + '\n' +
        open('CHANGES.rst').read() + '\n'
    ),
    name='buildout.bootstrap',
    namespace_packages=[
        'buildout'
    ],
    packages=find_packages(),
    test_suite='buildout.bootstrap.tests.TestBuildoutBootstrap',
    url='http://collective.github.com/buildout.bootstrap',
    version=VERSION,
    zip_safe=False,
)
