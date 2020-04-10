#!/usr/bin/python3

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.146.199.106', '18.212.79.62']


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
