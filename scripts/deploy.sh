#! /bin/bash

docker build --target production --tag "$DOCKER_USERNAME"/todo-app:"$TRAVIS_COMMIT" .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push "$DOCKER_USERNAME"/todo-app:"$TRAVIS_COMMIT"
docker tag "$DOCKER_USERNAME"/todo-app:"$TRAVIS_COMMIT" registry.heroku.com/devops-starter/web
echo "$HEROKU_API_KEY" | docker login -u "$HEROKU_USERNAME" --password-stdin registry.heroku.com
docker push registry.heroku.com/devops-starter/web
heroku container:release web --app=devops-starter