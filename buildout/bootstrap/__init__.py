import urllib

line = ('----------------------------------------' +
        '----------------------------------------')


def install(buildout, open_=None):
    """
    You know, I have one simple request. And that is to have sharks
    with frickin' laser beams attached to their heads! Actually, all
    I really want to do is avoid typing:

        $ curl -O https://raw.github.com/buildout/buildout/master/\
            bootstrap/bootstrap.py

    """
    url = 'https://raw.github.com/buildout/buildout'
    url += '/master/bootstrap/bootstrap.py'
    try:
        code = urllib.urlopen(url).getcode()
    except:
        # BBB Support Python 2.4
        import urllib2
        code = urllib2.urlopen(url).code
    if code == 200:
        data = urllib.urlopen(url).read()
        infile = '/'.join([buildout['buildout']['directory'], 'bootstrap.py'])
        if open_ is None:
            open_ = open
        bootstrap = open_(infile, 'w')
        bootstrap.write(data)
        bootstrap.close()
        print line
        print 'Downloading zc.buildout bootstrap.py file from:\n  %s' % url
        print 'To:\n  %s' % infile
        print line
    elif code == 404:
        print line
        print ('Unable to download zc.buildout bootstrap.py file from:\n  %s' %
            url)
        print 'Not found.'
        print line
    else:
        print line
        print ('Unable to download zc.buildout bootstrap.py file from:\n  %s' %
            url)
        print 'Unknown error code: %s' % code
        print line
