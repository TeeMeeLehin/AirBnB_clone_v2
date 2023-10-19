#!/usr/bin/python3
""" Fabfile to deploy web static folder"""
from datetime import datetime
from fabric.api import env, run, put, local
from os.path import exists

env.hosts = ['100.26.249.240', '54.159.22.198']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Create a .tgz archive from the contents of the web_static folder."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")

    archive_name = f"web_static_{timestamp}.tgz"

    zipped = local(f"tar -cvzf versions/{archive_name} web_static")

    if zipped.succeeded:
        return f"versions/{archive_name}"
    else:
        return None


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
        run(f"sudo mkdir -p {release_path}")
        run(f"sudo tar -xzf /tmp/{archive_filename} -C {release_path}")

        run(f"sudo rm /tmp/{archive_filename}")
        run(f"sudo mv {release_path}/web_static/* {release_path}/")
        run(f"sudo rm -rf {release_path}/web_static")

        current_link = '/data/web_static/current'
        run(f"sudo rm -rf {current_link}")

        run(f"sudo ln -s {release_path} {current_link}")

        return True
    except Exception:
        return False


def deploy():
    """Create and distribute an archive, then deploy it to web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
