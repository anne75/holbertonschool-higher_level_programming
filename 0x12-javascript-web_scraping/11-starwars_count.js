#!/usr/bin/node
const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, function (error, response, body) {
  if (!error) {
    let count = 0;
    for (const e of JSON.parse(body)['results']) {
      if (e['characters'].indexOf('http://swapi.co/api/people/18/') > -1) {
        count += 1;
      }
    }
    console.log(count);
  }
});
