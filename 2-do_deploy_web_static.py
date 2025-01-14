#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import env, put, run
import os.path

env.hosts = ["100.25.204.11", "52.3.245.182"]
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


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
        run("sudo mv {}/web_static/* {}".format(remote_folder, remote_folder))
        run("sudo rm -rf {}/web_static".format(remote_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} {}".format(remote_folder, symbolic_conn))
        return True
    except Exception as e:
        return False
