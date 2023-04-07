#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone'''

from datetime import datetime
from fabric.api import local


def do_pack():
    '''archive creation'''
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y%m%d%H%M%S")

    '''creating versions directory if it does not exists'''
    local('mkdir -p versions')

    '''tar && gzip creation'''
    archive_name = "web_static_{}.tgz".format(timestamp)
    res = local("tar -cvzf versions/{} web_static".format(archive_name))

    '''return the archive path if the archive has been correctly generated'''
    if res.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None
