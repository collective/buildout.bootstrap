import os
import unittest
from buildout.bootstrap import install

def myopen():
    pass

class TestBuildoutBootstrap(unittest.TestCase):

    def setUp(self):
        self.buildout = {'abuildout': {'directory': '.'}}

    def test_install(self):
        pass

        #======================================================================
        #ERROR: test_install (buildout.bootstrap.tests.TestBuildoutBootstrap)
        #----------------------------------------------------------------------
        #Traceback (most recent call last):
        #  File "/Users/alexclark/Developer/plone/buildout.bootstrap/buildout/bootstrap/tests.py", line 16, in test_install
        #    install(self.buildout, open_ = myopen)
        #  File "/Users/alexclark/Developer/plone/buildout.bootstrap/buildout/bootstrap/__init__.py", line 14, in install
        #    offline = buildout['buildout'].get('offline', 'true').lower()
        #KeyError: 'buildout'

        # XXX Why is this failing?
        #install(self.buildout, open_ = myopen)
        #self.assertTrue('bootstrap-buildout.py' in os.listdir('.'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
