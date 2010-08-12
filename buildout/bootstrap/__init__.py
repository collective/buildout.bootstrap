# -*- coding: utf-8 -*-
"""Recipe bootstrap"""

class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        """Installer"""
        # XXX Implement recipe functionality here

        # You know, I have one simple request. And that is to have sharks with 
        # frickin' laser beams attached to their heads! Actually all I really what to do is avoid:
        # svn cat svn://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py > bootstrap.py
        import urllib
        url = 'http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py'
        data = urllib.urlopen(url).read()
        file = '/'.join([self.buildout['buildout']['directory'],'bootstrap.py'])
        bootstrap_py = open(file,'w')
        bootstrap_py.write(data)
        bootstrap_py.close()

        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.
        return tuple()

    def update(self):
        """Updater"""
        pass
