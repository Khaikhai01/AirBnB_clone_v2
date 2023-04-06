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
    archieve_name = f'web_static_{timestamp}.tgz'
    res = local(f'tar -cvzf versions/{archive_name} web_static')

    '''return the archive path if the archive has been correctly generated'''
    if result.succeeded:
        return f'versions/{archive_name}'
    else:
        return None
