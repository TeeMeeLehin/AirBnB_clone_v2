#!/usr/bin/python3
""" Fabfile to compress web static folder"""
from fabric.api import local
from datetime import datetime


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
