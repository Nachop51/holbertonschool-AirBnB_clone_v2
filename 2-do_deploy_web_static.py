#!/usr/bin/python3
""" Fabric script to deploy in a web server """
from fabric.operations import run, put
from fabric.api import env
import os
env.hosts = ['34.227.46.143', '18.234.112.14']


def do_deploy(archive_path):
    """ Do deploy function distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return False
    filename = archive_path.split('/')[1][:-4]
    o1 = put(archive_path, "/tmp/{}.tgz".format(filename))
    o2 = run("mkdir -p /data/web_static/releases/{}/".format(filename))
    o3 = run("tar -zxf /tmp/{}.tgz -C /data/web_static/releases/{}/"
             .format(filename, filename))
    o4 = run("rm /tmp/{}.tgz".format(filename))
    o5 = run("rm -fr /data/web_static/current")
    o6 = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
             .format(filename))
    o7 = run("mv /data/web_static/releases/{}"
             "/web_static/* /data/web_static/releases/{}/"
             .format(filename, filename))
    for o in [o1, o2, o3, o4, o5, o6, o7]:
        if o.failed:
            return False
    return True
