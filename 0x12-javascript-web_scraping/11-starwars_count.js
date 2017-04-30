#!/usr/bin/node
// print the number of movies character 18 was present.
// the star wars api is passed on command line

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};
// const baseApi = process.argv[2].split('/').slice(0, -1).join('/');
request(options, function (error, response, body) {
  if (!error) {
    let count = 0;
    for (const e of JSON.parse(body)['results']) {
      for (const subE of e['characters']) {
        if (subE.includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
