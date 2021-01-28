#!/usr/bin/env bash

set -euo pipefail

docker-compose build >> /dev/null

pushd app/tests >> /dev/null
for i in $(ls test_*.py); do
    echo "Running ${i} tests..."
    docker run --rm -it flask-db-app:latest python /app/tests/$i
done
