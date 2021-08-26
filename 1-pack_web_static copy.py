#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime


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
