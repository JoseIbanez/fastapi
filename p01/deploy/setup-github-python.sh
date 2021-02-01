#!/bin/bash

pwd
export
ls -l

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-test.txt

pip list

