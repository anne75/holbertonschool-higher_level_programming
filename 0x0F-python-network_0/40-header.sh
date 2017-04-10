#!/usr/bin/env bash
# pass a custome header variable in a GET request
curl -LX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
