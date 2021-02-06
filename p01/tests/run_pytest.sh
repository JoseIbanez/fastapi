#!/bin/bash
PROJECT=cifastapi

echo 
echo "PyTest"
python -m pytest . \
    --cov-fail-under=80 -v \
    --doctest-modules --junitxml=junit/test-results.xml \
    --cov=$PROJECT --cov-report=xml --cov-report=html --cov-report=term

