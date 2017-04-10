#!/bin/bash
# pass a custom header variable in a GET request
curl -sLX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
