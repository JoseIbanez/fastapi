#!/bin/bash

#exit on first error
set -e



ver=$(head -n 1 "./VERSION")

# Gitlab pipeline
if [ "$CI_JOB_ID" ]
then
      echo "${ver}.dev$CI_JOB_ID"
      echo "${ver}.dev$CI_JOB_ID" > ./VERSION
fi

# Azure pipeline
if [ "$BUILD_BUILDNUMBER" ]
then
      echo "${ver}.dev$BUILD_BUILDNUMBER"
      echo "${ver}.dev$BUILD_BUILDNUMBER" > ./VERSION
fi


cat ./VERSION
echo $ver > ./VERSION


cd ..
# Remove old version
rm -rf build/ dist/

# To create a dist
python setup.py sdist bdist_wheel

# To upload to PyPI
python -m twine check dist/*
#python -m twine upload dist/*