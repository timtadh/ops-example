Vagrant.configure(2) do |config|
  config.vm.box = "precise64_updated_20130329"
  config.vm.network :forwarded_port, guest: 22, host: 2222, id: "ssh"
  config.ssh.port = 2222
  config.vm.network :forwarded_port, guest: 80, host: 8000, id: "web"
end
