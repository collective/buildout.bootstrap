from setuptools import setup, find_packages

setup (
    name = 'buildout.bootstrap',
    packages = find_packages(),
    install_requires = ['setuptools'],
    namespace_packages = ['buildout'],
    entry_points = {"zc.buildout.extension": ["default = buildout.bootstrap:install"]}
)
