#!/usr/bin/python3   
from fabric.api import env, put, run
import os.path
 
env.hosts = ["100.25.204.11", "52.3.245.182"]
 
def do_deploy(archive_path):
    ''' checking is file path exists'''
    if not os.path.isfile(archive_path):
        return False
    compressed = archive_path.split("/")[-1]
    uncompressed_path = compressed.split(".")[0]
   
    try:
        remote_folder = "/data/web_static/releases/{}/".format(uncompressed_path)

        symbolic_conn = "/data/web_static/current"

        put(archive_path, "/tmp/")

        run("mkdir - p {}".format(remote_folder))

        run("tar -xvzf /tmp/{} -C {}".format(compressed, remote_folder))

        run("rm /tmp/{}".format(compressed))

        run("ln -sf {} {}".format(remote_folder, symbolic_conn))
        return True
    except Exception as e:
        return False
