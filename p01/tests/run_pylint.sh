#!/bin/bash

#exit on first error
set -e

PROJECT=cifastapi

echo 
echo "Pylint"
cd ..
pylint --disable=R0801,C0103 \
    --fail-under 8.5 \
    $PROJECT/*.py
    
#    || \
#    pylint-exit --error-fail $? 