#!/bin/bash
set -e {0}

sudo apt-get update -y
sudo apt-get install -y python3 python3-pip

pip3 install --upgrade keyrings.alt
sudo pip3 install --upgrade pip
pip3 install --upgrade setuptools wheel twine
pip3 install --upgrade --ignore-installed PyYAML
pip3 install --upgrade ansible

ansible-galaxy collection install community.docker
