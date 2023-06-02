#!/bin/bash

set -e
echo "Executing 'git pull'"
git stash
git pull

echo "Starting dockers"
docker compose up -d

echo "Collect static files"
sudo cp -r /var/lib/docker/volumes/docker-star-burger_static/_data /var/lib/docker/volumes/docker-star-burger_frontend
sudo cp -r /var/lib/docker/volumes/docker-star-burger_static/_data/bundles /var/lib/docker/volumes/docker-star-burger_frontend


echo "Reporting to Rollbar"
export $(xargs < ./.env)
REVISION=$(git rev-parse --short HEAD)

curl "https://api.rollbar.com/api/1/deploy/" \
     -F access_token=$ROLLBAR_ACCESS_TOKEN \
     -F environment=$ROLLBAR_ENVIRONMENT \
     -F revision=$REVISION \
     -F local_username="root"

echo
echo "Deployed successfully"
