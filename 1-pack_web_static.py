#!/usr/bin/python3
"""do packing"""
from fabric.api import *
from datetime import datetime
from os.path import isdir


def do_pack():
    """packing stuff"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if isdir("versions") is False:
        local("mkdir versions")
    name = "versions/web_static_{}.tgz".format(date)
    try:
        local("tar -cvzf {} web_static".format(name))
        return name
    except Exception as e:
        return None
