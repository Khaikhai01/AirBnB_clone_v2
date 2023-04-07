#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone'''

from fabric.api import env, put, run, local
import os.path
from datetime import datetime

env.hosts = ["100.25.204.11", "52.3.245.182"]
env.private_key = '~/.ssh/school'
env.usr_name = 'ubuntu'


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


def do_deploy(archive_path):
    ''' checking is file path exists'''
    if not os.path.isfile(archive_path):
        return False
    compressed = archive_path.split("/")[-1]
    uncompressed = compressed.split(".")[0]

    try:
        remote_folder = "/data/web_static/releases/{}/".format(uncompressed)

        symbolic_conn = "/data/web_static/current"

        put(archive_path, "/tmp/")

        run("sudo mkdir -p {}".format(remote_folder))

        run("sudo tar -xvzf /tmp/{} -C {}".format(compressed, remote_folder))

        run("sudo rm /tmp/{}".format(compressed))
        run('sudo mv {}/web_static/* {}'.format(remote_folder, remote_folder))
        run('sudo rm -rf {}/web_static'.format(remote_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -sf {} {}".format(remote_folder, symbolic_conn))
        return True
    except Exception as e:
        return False


def deploy():
    '''full deployment'''
    pathArchieved = do_pack()
    if pathArchieved is not None:
        return do_deploy(pathArchieved)
    return False
