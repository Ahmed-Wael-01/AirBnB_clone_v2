#!/usr/bin/python3
"""Generates a .tgz archive and distributes the archive to the web servers"""

from fabric.api import run, env, put
from os import path

env.hosts = ['54.209.62.255', '52.23.179.43']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes the .tgz archive to the web servers"""

    if not path.exists(archive_path):
        return False

    try:
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/{}".format(
            archived_file[:-4])
        archived_file = "/tmp/{}".format(archived_file)

        put(archive_path, "/tmp/")
        sudo("sudo mkdir -p {}".format(newest_version))
        sudo("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        sudo("sudo rm {}".format(archived_file))
        sudo("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        sudo("sudo rm -rf {}/web_static".format(newest_version))
        sudo("sudo rm -rf /data/web_static/current")
        sudo("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")

        return True
    except Exception:
        return False
