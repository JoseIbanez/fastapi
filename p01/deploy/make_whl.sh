#!/bin/bash
set -e

cd ..
# Remove old version
rm -rf build/ dist/

# To create a dist
python setup.py sdist bdist_wheel

# To upload to PyPI
python -m twine check dist/*
#python -m twine upload dist/*