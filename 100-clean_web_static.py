#!/usr/bin/python3
"""Fabfile  that deletes out-of-date archives"""
from fabric.api import env, run, local, task
from datetime import datetime
from os import listdir
from os.path import isfile, join

env.hosts = ['54.160.126.192', '54.159.22.198']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """Delete out-of-date archives from versions and releases folders."""

    number = 1 if int(number) == 0 else int(number)
    archive_dir = 'versions'
    LA = [f for f in listdir(archive_dir) if isfile(join(archive_dir, f))]

    LA.sort(reverse=True)

    archives_to_delete = LA[number:]
    for archive in archives_to_delete:
        local("rm -f {}/{}".format(archive_dir, archive))

    releases_dir = '/data/web_static/releases'
    releases = run("ls -1 {}".format(releases_dir)).split('\n')

    releases_to_delete = releases[number:]
    for release in releases_to_delete:
        if release != 'test':
            run("rm -rf {}/{}".format(releases_dir, release))

    return True
