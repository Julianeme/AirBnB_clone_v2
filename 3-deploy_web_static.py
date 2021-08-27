#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""

import os
from fabric.api import put
from fabric.api import env
from fabric.api import run
from fabric.api import local
from datetime import datetime

env.hosts = ['34.73.56.44', '54.234.202.244']


def do_pack():
    """
    Creates a versions folder and a tar archive of the web_static directory
    """

    try:
        local('mkdir -p versions')
        created_at = datetime.now().strftime("%Y-%m-%d%H%M%S")
        file_name = str('web_static_' + created_at)
        file_path = 'versions/' + file_name
        local('tar -cvzf {}.tgz web_static'.format(file_path))
        return(file_path)
    except:
        return None


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
            /data/web_static/releases/{}/'.format(filename, filename))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(filename))
        return(True)
    except:
        return(False)


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    try:
        archive_path = do_pack()
        return do_deploy(archive_path)
    except:
        return False
