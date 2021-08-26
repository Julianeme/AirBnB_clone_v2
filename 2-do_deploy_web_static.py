#!/usr/bin/python3
"""
script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers
"""

from fabric.api import put, env, hosts, run
import os

env.hosts = ['34.73.56.44', '54.234.202.244']


def do_deploy(archive_path):
    # verificamos si el path existe
    if os.path.exists(archive_path) is False:
        return(False)
    try:
        # Upload the archive to the / tmp / directory of the web server
        put(archive_path, '/tmp/')
        # get the filename in the following 2 lines
        filename_ext = archive_path.split("/")[-1]
        filename = filename_ext.split(".")[0]
        # Uncompress the archive to folder /data/web_static/releases/<archive
        run('tar zxvf /tmp/{} /data/web_static/releases/{}'.format
            (filename_ext, filename))
        # Delete the archive from the web server
        run(f'rm -r /tmp/{}'.format(filename_ext))
        # Delete the symbolic link /data/web_static/current from the web server
        run('rm /data/web_static/current')
        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension >
        run('ln -s / data/web_static/releases/{} /data/web_static/current'
            .format(filename))
        return(True)
    except:
        return(False)
