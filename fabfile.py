from fabric import api

def who():
    api.run('echo $(whoami) on $(uname -s)')

def bootstrap():
    api.sudo('apt-get update')
    api.sudo('apt-get install --yes build-essential')

def provision():
    provision_app()

def config():
    config_app()

def deploy():
    deploy_app()

def provision_nginx():
    api.sudo('apt-get install --yes nginx')
    api.sudo('rm /etc/nginx/sites-enabled/default')

def provision_app():
    provision_nginx()
    api.sudo('apt-get install --yes python-dev python-pip')
    api.sudo('pip install virtualenv')
    api.run('mkdir -p $HOME/app')
    api.run('virtualenv --no-site-packages $HOME/app/env')

def config_app():
    api.put('production.ini', 'app/production.ini')
    api.put('startup.conf', 'startup.conf')
    api.sudo('mv startup.conf /etc/init/app.conf')
    api.sudo('chown root:root /etc/init/app.conf')
    api.put('nginx-site.conf', 'nginx-site.conf')
    api.sudo('mv nginx-site.conf /etc/nginx/sites-available/app.conf')
    api.sudo('chown root:root /etc/nginx/sites-available/app.conf')
    api.sudo('test -e /etc/nginx/sites-enabled/app.conf || ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf')
    api.sudo('service nginx restart')
    api.run('source app/env/bin/activate && pip install uwsgi flask')

def deploy_app():
    api.local('tar czf app.tar.gz app/')
    api.put('app.tar.gz', 'app/app.tar.gz')
    api.run('cd app/ && tar xzf app.tar.gz')
    api.sudo('service app restart')

