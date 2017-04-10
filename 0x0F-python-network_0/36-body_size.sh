#!/bin/bash
# gets the content-length header
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
