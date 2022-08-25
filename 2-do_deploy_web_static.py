#!/usr/bin/python3
""" Fabric script to deploy in a web server """
from fabric.operations import run, put, local
from fabric.api import env
from datetime import datetime as dt
import os
env.hosts = ['34.227.46.143', '18.234.112.14']


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


def do_deploy(archive_path):
    """ Do deploy function distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return False
    filename = archive_path.split('/')[1][:-4]
    o1 = put(archive_path, "/tmp/{}.tgz".format(filename))
    if o1.failed:
        return False
    o2 = run("mkdir -p /data/web_static/releases/{}/".format(filename))
    if o2.failed:
        return False
    o3 = run("tar -zxf /tmp/{}.tgz -C /data/web_static/releases/{}/"
             .format(filename, filename))
    if o3.failed:
        return False
    o4 = run("rm /tmp/{}.tgz".format(filename))
    if o4.failed:
        return False
    o5 = run("mv /data/web_static/releases/{}"
             "/web_static/* /data/web_static/releases/{}/"
             .format(filename, filename))
    if o5.failed:
        return False
    o6 = run("rm -rf /data/web_static/releases/{}/web_static"
             .format(filename))
    if o6.failed:
        return False
    o7 = run("rm -rf /data/web_static/current")
    if o7.failed:
        return False
    o8 = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
             .format(filename))
    if o8.failed:
        return False
    o9 = run("mv /data/web_static/releases/{}"
             "/web_static/* /data/web_static/releases/{}/"
             .format(filename, filename))
    if o9.failed:
        return False
    print('New version deployed!')
    return True
