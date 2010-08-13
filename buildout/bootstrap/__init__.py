import urllib
import zc.buildout.easy_install

logger = zc.buildout.easy_install.logger

def install(buildout):
    """
    You know, I have one simple request. And that is to have sharks with 
    frickin' laser beams attached to their heads! 
    
    Actually, all I really want is to avoid typing:

        $ wget http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py

    """

    url = 'http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py'
    data = urllib.urlopen(url).read()
    file = '/'.join([self.buildout['buildout']['directory'],'bootstrap.py'])
    bootstrap_py = open(file,'w')
    bootstrap_py.write(data)
    bootstrap_py.close()

#    file_name = 'dump-picked-versions-file' in buildout['bootstrap'] and \
#                buildout['buildout']['dump-picked-versions-file'].strip() or \
#                None
#                
#    overwrite = 'overwrite-picked-versions-file' not in buildout['buildout'] or \
#                buildout['buildout']['overwrite-picked-versions-file'].lower() \
#                in ['yes', 'true', 'on']
#
#    zc.buildout.easy_install.Installer.__picked_versions = {}
#    zc.buildout.easy_install._log_requirement = _log_requirement
#    zc.buildout.easy_install.Installer._get_dist = enable_dumping_picked_versions(
#                                  zc.buildout.easy_install.Installer._get_dist)
#    
#    logging.shutdown = dump_picked_versions(logging.shutdown, 
#                                            file_name, 
#                                            overwrite)
#
