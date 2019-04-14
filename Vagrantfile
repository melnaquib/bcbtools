Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu1804"


  config.vm.synced_folder ".", "/home/vagrant/bcbtools/"


  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = true

    vb.name = "Bitcoin Black Tools"
    vb.cpus = 2
    # Customize the amount of memory on the VM:
    vb.memory = "2048"
    vb.customize ["modifyvm", :id, "--accelerate3d", "on"]
    vb.customize ["modifyvm", :id, "--vram", "128"]

    # Enable the shared clipboard:
    vb.customize ['modifyvm', :id, '--clipboard', 'bidirectional']  end

    # config.vm.network "public_network", type: "dhcp"


  # Install xfce and virtualbox additions
  config.vm.provision "shell", inline: "sudo apt-get update"
  config.vm.provision "shell", inline: "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y xfce4 xfce4-terminal \
    virtualbox-guest-dkms virtualbox-guest-utils virtualbox-guest-x11 \
    lightdm lightdm-gtk-greeter"
  # Permit anyone to start the GUI
  config.vm.provision "shell", inline: "sudo sed -i 's/allowed_users=.*$/allowed_users=anybody/' /etc/X11/Xwrapper.config"
  config.vm.provision "shell", inline: "sudo VBoxClient --clipboard && sudo VBoxClient --draganddrop && sudo VBoxClient --display && sudo VBoxClient --checkhostversion && sudo VBoxClient --seamless"

  config.vm.provision "shell", inline: "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y curl geany aptitude synaptic \
    build-essential cmake gdb dh-autoreconf libgl1-mesa-dev pkg-config python-zmq libzmq3-dev libxslt1.1 git \
    python python-dev python-wheel python-pip python-setuptools \
    python3 python3-dev python3-wheel python3-pip python3-setuptools \
    libegl1-mesa mesa-utils libxcb-icccm4 libxcb-render-util0 libxkbcommon-x11-0 \
    libxcb-image0 libxcb-keysyms1 libxcb-xkb1 libdouble-conversion1"


  config.vm.provision :shell, :path => "scripts/btcb_node_install.sh", :args => ENV['BTCB_NETWORK']

  config.vm.provision "shell", inline: "sudo -H pip3 install -r /home/vagrant/bcbtools/requirements.txt"

  config.vm.provision "file", source: "config/config.json", destination: "~/Btcb/config.json"
  config.vm.provision "file", source: "config/config.json", destination: "~/BtcbBeta/config.json"
  config.vm.provision "file", source: "BcbTools.desktop", destination: "~/Desktop/BcbTools.desktop"

#  config.vm.provision "file", source: "config/lightdm.conf", destination: "/tmp/lightdm.conf"
#  config.vm.provision "shell", inline: "sudo cp /tmp/lightdm.conf /etc/lightdm/lightdm.conf.d/"


  # config.vm.provision :reload


  # config.vm.provision "shell", inline: "startxfce4 &"
  config.vm.provision "shell", inline: "sudo -H /etc/init.d/lightdm start"

end
