import urllib


def install(buildout):
    """
    You know, I have one simple request. And that is to have sharks with
    frickin' laser beams attached to their heads!

    Actually, all I really want is to avoid typing:

        $ wget http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/\
            bootstrap.py

    """
    base = 'http://svn.zope.org'
    url = base + '/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py'
    data = urllib.urlopen(url).read()
    file = '/'.join([buildout['buildout']['directory'], 'bootstrap.py'])
    bootstrap = open(file, 'w')
    bootstrap.write(data)
    bootstrap.close()

    print ('----------------------------------------' +
            '----------------------------------------')
    print 'Downloading zc.buildout bootstrap.py file from:\n  %s' % url
    print 'To:\n  %s' % file
    print ('----------------------------------------' +
            '----------------------------------------')
