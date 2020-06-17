#!/bin/dash
set -e

SERIALIZER_FILE_NAME=$1
if [ -z "$SERIALIZER_FILE_NAME" ]; then
    echo "Usage: docker.sh SERIALIZER_FILE_NAME"
    exit 1
fi

CONTAINER_NAME=radiation-counting-ml

printf "\nremoving container if it exists...\n"
docker rm -f $CONTAINER_NAME || true

printf "\nbuilding container...\n"
docker build . \
    --tag $CONTAINER_NAME

printf "\nrunning container...\n"
docker run \
    --name $CONTAINER_NAME \
    -v "$PWD/data:/usr/src/app/data:ro" \
    "$CONTAINER_NAME" "$SERIALIZER_FILE_NAME"
