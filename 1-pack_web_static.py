#!/usr/bin/python3

from datetime import datetime
from fabric.api import local
from os import path


def do_pack():
    '''This function generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo'''
    now = datetime.utcnow()
    tarName = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                            now.month,
                                                            now.day,
                                                            now.hour,
                                                            now.minute,
                                                            now.second)

    if not path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local('tar -cvzf {} web_static'.format(tarName)).failed:
        return None
    return tarName
