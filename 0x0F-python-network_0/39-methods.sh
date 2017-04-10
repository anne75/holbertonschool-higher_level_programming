#!/bin/bash
# make an OPTIONS request
curl -siLX OPTIONS "$1" | grep "Allow:" | cut -b8-
