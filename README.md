# ops-example

By Tim Henderson (tim.tadh@gmail.com)

Licensed Under BSD 3-Clause.

## Slides

Read the (slides)[Infrastructure with Ansible.pdf]

## Setup Vagrant

```bash
$ git clone https://github.com/timtadh/ops-example.git
$ cd ops-example
$ vagrant box add ubuntu/trusty64 https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box
$ vagrant up
```

## Setup SSH Config

```
$ vagrant ssh-config | sed 's/^Host default$/Host vagrant/' >> ~/.ssh/config
$ ssh-add ~/.vagrant.d/insecure_private_key
```

## Setup Virtualenv

```bash
$ virtualenv --no-site-packages env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Great, you are ready to role.

## Fabric Version

```bash
$ fab -H vagrant@localhost:2222 who
[vagrant@localhost:2222] Executing task 'who'
[vagrant@localhost:2222] run: echo $(whoami) on $(uname -s)
[vagrant@localhost:2222] out: vagrant on Linux
[vagrant@localhost:2222] out: 


Done.
Disconnecting from vagrant@localhost:2222... done.
```

Great we have connectivity, let's run it.

```bash
$ fab -H vagrant@localhost:2222 bootstrap provision config deploy
....
```

Now browse in your web browser to <http://127.0.0.1:8000> you should see *Hello World*.

## Ansible Version

First destroy and recreate the environment

```bash
$ vagrant halt
$ vagrant destory
$ vagrant up
```

Now run the playbooks

```bash
$ ansible-playbook -i HOSTS bootstrap.yml provision.yml config.yml deploy.yml
```

Now browse in your web browser to <http://127.0.0.1:8000> you should see *Hello World*.

