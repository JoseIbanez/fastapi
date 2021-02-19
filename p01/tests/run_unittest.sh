#!/bin/bash

#exit on first error
set -e

sudo mkdir -p /etc/cifastapi
sudo cp ../cifastapi/VERSION_FULL   /etc/cifastapi/
sudo cp ../cifastapi/file.config    /etc/cifastapi/
sudo chmod 755 /etc/cifastapi/*

echo 
echo "Unittest"
python -m unittest discover -v -b