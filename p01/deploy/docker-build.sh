#!/bin/bash

VERSION=`head -n 1 ./VERSION`

cp requirements.txt ../cifastapi/
cd ../cifastapi/
TAG="$VERSION-rc.`date +%s`"
echo "Build version: $TAG"
docker build . -t ibanez/vmdeployments:$TAG -t ibanez/vmdeployments:dev-latest


if [ -v DOCKER_USER ] && [ -v DOCKER_PASS ]
then
   echo $DOCKER_PASS | docker login --username $DOCKER_USER --password-stdin
   docker push ibanez/vmdeployments:dev-latest
   docker push ibanez/vmdeployments:$TAG
fi