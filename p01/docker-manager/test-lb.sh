#!/bin/bash

for x in {1..2000}
do 
    curl 127.0.0.1?token=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1) &
    sleep 0.1
    echo
done