from setuptools import find_packages
from setuptools import setup


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Zope Public License',
    ],
    description='A buildout extension that adds a buildout\
        bootstrap.py file to your buildout.',
    entry_points={
        "zc.buildout.extension": [
            "default = buildout.bootstrap:install"
        ]
    },
    license='ZPL',
    name='buildout.bootstrap',
    version='1.2',
    long_description=(
        open('README.rst').read() +
        open('docs/INSTALL.txt').read() +
        open('docs/HISTORY.txt').read() +
        open('docs/CONTRIBUTORS.txt').read()
    ),
    keywords='buildout bootstrap',
    url='http://collective.github.com/buildout.bootstrap',
    packages=find_packages(),
    namespace_packages=['buildout'],
)
