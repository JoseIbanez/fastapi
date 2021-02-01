#!/bin/bash

#exit on first error
set -e

echo 
echo "Unittest"
python -m unittest discover -v -b