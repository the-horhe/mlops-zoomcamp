#!/usr/bin/env bash
set -uoe pipefail

docker build --tag web_service .
docker run --rm -d --network host web_service
