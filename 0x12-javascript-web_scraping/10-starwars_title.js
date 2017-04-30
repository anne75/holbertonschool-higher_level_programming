#!/usr/bin/node
// print the title of a star wars movie depending on command line argument

const request = require('request');
const options = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  method: 'GET'
};
request(options, function (error, response, body) {
  if (!error) {
    console.log(JSON.parse(body)['title']);
  }
});
