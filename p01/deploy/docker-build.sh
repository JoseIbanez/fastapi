#!/bin/bash
set -e

TAG=`head -n 1 ./VERSION_FULL`

cp requirements.txt ../cifastapi/
cd ../cifastapi/

echo "Build version: $TAG"
docker build . -t ibanez/vmdeployments:$TAG -t ibanez/vmdeployments:dev-latest


if [ -v DOCKER_USER ] && [ -v DOCKER_PASS ]
then
   echo $DOCKER_PASS | docker login --username $DOCKER_USER --password-stdin
   docker push ibanez/vmdeployments:dev-latest
   docker push ibanez/vmdeployments:$TAG
fi
