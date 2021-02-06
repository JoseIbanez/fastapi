#!/bin/bash

pwd
export
ls -l

#Prepare pip
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel twine
pip install --upgrade --ignore-installed PyYAML

#Install requirements
pip install -r requirements.txt
pip install -r requirements-test.txt
pip install -e ..

pip list

