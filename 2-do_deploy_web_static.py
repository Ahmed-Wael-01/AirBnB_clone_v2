#!/usr/bin/python3
"""do packing"""
from fabric.api import *
from os.path import exists
env.hosts = ['54.209.62.255', '52.23.179.43']


def do_deploy(archive_path):
    """packing stuff"""
    if exists(archive_path) is False:
        return False
    try:
        zfile = archive_path.split('/')[-1]
        unexe = zfile.split('.')[0]
        put(archive_path, '/tmp/')
        sudo('mkdir -p {}{}/'.format('/data/web_static/releases/', unexe))
        sudo('tar -xzf /tmp/{} -C {}{}/'.format(
                    zfile, '/data/web_static/releases/', unexe))
        sudo('rm /tmp/{}'.format(zfile))
        sudo('mv {0}{1}/web_static/* {0}{1}/'.format(
            '/data/web_static/releases/', unexe))
        sudo('rm -rf {}{}/web_static'.format(
            '/data/web_static/releases/', unexe))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}{}/ /data/web_static/current'.format(
            '/data/web_static/releases/', unexe))
        return True
    except Exception as e:
        return False
