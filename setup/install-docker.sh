#!/bin/bash

# if any arguments are specified, start by uninstalling docker-compose & docker
if [ $# -gt 0 ]
  then
    # uninstall docker-compose
    sudo rm /usr/local/bin/docker-compose

    # uninstall docker
    sudo apt-get remove docker docker-engine docker.io
fi

# install docker (https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository)
sudo apt-get update

sudo apt-get install -yq apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt-get update
sudo apt-get install docker-ce
sudo docker run hello-world

# install docker-compose (https://docs.docker.com/compose/install/ )
sudo curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version