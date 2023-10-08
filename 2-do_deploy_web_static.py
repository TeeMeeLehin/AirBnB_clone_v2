#!/usr/bin/python3
""" Fabfile to deploy web static folder"""
from fabric.api import env, run, put, local
from os.path import exists

env.hosts = ['54.160.126.192', '54.159.22.198']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distribute and deploy an archive to web servers."""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_filename = archive_path.split('/')[-1]
        archive_name_no_ext = archive_filename.split('.')[0]
        release_path = f"/data/web_static/releases/{archive_name_no_ext}"
        run(f"rm -rf {release_path}")
        run(f"mkdir -p {release_path}")
        run(f"tar -xzf /tmp/{archive_filename} -C {release_path}")

        run(f"rm /tmp/{archive_filename}")
        run(f"mv {release_path}/web_static/* {release_path}/")
        run(f"rm -rf {release_path}/web_static")

        current_link = '/data/web_static/current'
        run(f"rm -rf {current_link}")

        run(f"ln -s {release_path} {current_link}")

        return True
    except Exception:
        return False
