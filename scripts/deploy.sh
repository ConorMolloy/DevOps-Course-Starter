#! /bin/bash

docker build --target production --tag "$DOCKER_USERNAME"/todo-app:"$TRAVIS_COMMIT" .
docker tag "$DOCKER_USERNAME"/todo-app:"$TRAVIS_COMMIT" "$DOCKER_USERNAME"/todo-app
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push "$DOCKER_USERNAME"/todo-app:"$TRAVIS_COMMIT"
docker push "$DOCKER_USERNAME"/todo-app
curl -dH -X POST "$AZURE_WEBHOOK"