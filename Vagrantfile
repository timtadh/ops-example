Vagrant.configure(2) do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.network :forwarded_port, guest: 22, host: 2222, id: "ssh"
  config.ssh.port = 2222
  config.vm.network :forwarded_port, guest: 80, host: 8000, id: "web"
end
