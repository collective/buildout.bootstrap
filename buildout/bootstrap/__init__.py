import urllib

line = '-' * 80
truthiness = ('true', 'yes', 'on')
filename = 'bootstrap-buildout.py'


def install(buildout, open_=None):
    """
    You know, I have one simple request. And that is to have sharks
    with frickin' laser beams attached to their heads! Actually, all
    I really want to do is avoid having to download bootstrap.py.
    """
    offline = buildout['buildout'].get('offline', 'true').lower()
    if offline in truthiness:
        print 'Not updating bootstrap.py because buildout is in offline mode.'
        return
    url = 'https://bootstrap.pypa.io/%s' % filename
    try:
        code = urllib.urlopen(url).getcode()
    except IOError, e:
        if len(e.args) > 1:
            # Not so cool, but it works for 404
            code = e.args[1]
    except AttributeError:
        # BBB Support Python 2.4
        import urllib2
        code = urllib2.urlopen(url).code
    if code == 200:
        data = urllib.urlopen(url).read()
        infile = '/'.join([buildout['buildout']['directory'], filename])
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
