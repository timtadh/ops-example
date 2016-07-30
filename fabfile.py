from fabric import api

def who():
    api.run('echo $(whoami) on $(uname -s)')

