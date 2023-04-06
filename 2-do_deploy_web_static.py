from fabric.api import env, put, run
import os.path
 
env.hosts = ["100.25.204.11", "52.3.245.182"]
 
def do_deploy(archive_path):
   ''' checking is file path exists'''
    if not os.path.isfile(archive_path):
        return False
    compressed = archived_path.split("/")[-1]
    uncompressed_path = compressed.split(".")[0]
   
    try:
        remote_folder = f"/data/web_static/releases/{uncompressed_path}"

        symbolic_conn = "/data/web_static/current"

        put(archive_path, "/tmp/")

        run(f"mkdir - p {remote_folder}")

        run(f"tar -xvzf /tmp/{compressed} -C {remote_folder}")

        run(f"rm /tmp/{compressed}")

        run(f"ln -sf {remote_folder} {symbolic_conn}")
        return True
    except Exception as e:
        return False
