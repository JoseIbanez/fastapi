#!/bin/bash

#exit on first error
set -e

PROJECT=cifastapi

echo 
echo "Pylint"
cd ..
pylint --disable=R0801,C0103 $PROJECT/*.py || pylint-exit $?