#!/usr/bin/env bash

set -euo pipefail

docker-compose build
docker run --rm -it flask-db-app:latest python -m unittest discover -s tests -p 'test_*.py'
