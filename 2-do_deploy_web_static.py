#!/usr/bin/python3
"""
script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers
"""

from fabric.api import put, env, run
import os

env.hosts = ['34.73.56.44', '54.234.202.244']


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    # verificamos si el path existe
    if os.path.exists(archive_path) is False:
        return(False)
    try:
        filename_ext = archive_path.split("/")[-1]
        filename = filename_ext.split(".")[0]
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(filename))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format
            (filename_ext, filename))
        run('rm /tmp/{}'.format(filename_ext))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(filename))
        run('rm -rf /data/web_static/releases/{}/web_static{}'
            .format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(filename))
        return(True)
    except:
        return(False)
