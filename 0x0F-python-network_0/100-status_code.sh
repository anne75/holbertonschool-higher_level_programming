#!/bin/bash
# only get the http_code of a request response
curl -sLw "%{http_code}" -o /dev/null "$1"
