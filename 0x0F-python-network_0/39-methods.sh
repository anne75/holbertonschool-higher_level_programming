#!/usr/bin/env bash
# make an OPTIONS request
curl -siX OPTIONS "$1" | grep "Allow:" | cut -b8-
