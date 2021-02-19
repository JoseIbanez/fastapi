#!/bin/bash
set -e
ver=$(head -n 1 "./VERSION")

# Gitlab pipeline
if [ "$CI_JOB_ID" ]
then
    VERSION="${ver}-rc.$CI_JOB_ID"
fi

# Github pipeline
if [ "$GITHUB_SHA" ]
then
    VERSION="${ver}-rc.$GITHUB_SHA"
fi

# Azure pipeline
if [ "$BUILD_BUILDNUMBER" ]
then
    VERSION="${ver}-rc.$BUILD_BUILDNUMBER"
fi

# Else (local)
if [ ! "$VERSION" ]
then
    VERSION="${ver}-rc.`date +%s`"
fi

echo $VERSION > ./VERSION_FULL
echo $VERSION > ../cifastapi/VERSION_FULL

