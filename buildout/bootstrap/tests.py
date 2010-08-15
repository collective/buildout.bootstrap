import os
import unittest
from buildout.bootstrap import install

def myopen():
    pass

class TestBuildoutBootstrap(unittest.TestCase):

    def setUp(self):
        self.buildout = {'abuildout': {'directory': '.'}}

    def test_install(self):
        install(self.buildout, open_ = myopen)
        self.assertTrue('bootstrap.py' in os.listdir('.'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
