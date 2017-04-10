#!/usr/bin/env bash
# gets the content-lenght header
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
