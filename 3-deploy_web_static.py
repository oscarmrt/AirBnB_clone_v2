#!/usr/bin/python3

from datetime import datetime
from fabric.api import put, run, env, local
from os.path import exists, isdir
env.hosts = ['54.146.199.106', '18.212.79.62']


def do_pack():
    '''This function generates a .tgz archive from the
    contents of the web_static folder of your AirBnB
    Clone repo'''
    now = datetime.utcnow()
    tarName = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                            now.month,
                                                            now.day,
                                                            now.hour,
                                                            now.minute,
                                                            now.second)

    if not isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local('tar -cvzf {} web_static'.format(tarName)).failed:
        return None
    return tarName


def do_deploy(archive_path):
    '''distributes an archive to your web servers'''
    if exists(archive_path) is False:
        return False
    try:
        tarName = archive_path.split("/")[-1]
        remExt = tarName.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, remExt))
        run('tar -xzf /tmp/{} -C {}{}/'.format(tarName, path, remExt))
        run('rm /tmp/{}'.format(tarName))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, remExt))
        run('rm -rf {}{}/web_static'.format(path, remExt))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, remExt))
        return True
    except:
        return False


def deploy():
    '''creates and distributes an archive to your web servers'''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
