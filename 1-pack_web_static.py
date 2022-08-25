#!/usr/bin/python3.4
from datetime import datetime as dt
from fabric.operations import local
""" Module that creates a folder and a tgz file """


def do_pack():
    """ Compress a directory into a tgz and creates a directory """
    local("mkdir -p versions")
    now = dt.now().strftime("%Y%m%d%H%M%S")
    file_output = local(
        "tar -vczf versions/web_static_{}.tgz web_static".format(now),
        capture=True
    )
    return file_output if not file_output.failed else None
