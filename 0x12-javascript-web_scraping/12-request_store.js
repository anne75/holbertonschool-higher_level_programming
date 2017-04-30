#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options).pipe(fs.createWriteStream(process.argv[3], 'utf8'));
