import os
import unittest
from buildout.bootstrap import install


class TestBuildoutBootstrap(unittest.TestCase):

    def setUp(self):
        self.buildout = {'buildout': {'directory': '.'}}

    def test_install(self):
        install(self.buildout)
        self.assertTrue('bootstrap.py' in os.listdir('.'))

if __name__ == '__main__':
    unittest.main()
