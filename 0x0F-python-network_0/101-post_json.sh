#!/bin/bash
# send a JSON POST request, the json being in a file
curl -sLH "Content-Type: application/json" -d @"$2" "$1"
