from setuptools import find_packages
from setuptools import setup
import os


VERSION = '1.4.6'


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
    description='A buildout extension that adds a buildout\
        bootstrap.py file to your buildout.',
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
        open(os.path.join('docs', 'INSTALL.txt')).read() + '\n' +
        open(os.path.join('docs', 'HISTORY.txt')).read() + '\n' +
        open(os.path.join('docs', 'CONTRIBUTORS.txt')).read()
    ),
    name='buildout.bootstrap',
    namespace_packages=[
        'buildout'
    ],
    packages=find_packages(),
    url='http://collective.github.com/buildout.bootstrap',
    version=VERSION,
    zip_safe=False,
)
