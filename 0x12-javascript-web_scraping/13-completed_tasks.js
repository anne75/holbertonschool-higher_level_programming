#!/usr/bin/node
// compute the number of tasks completed by users with
// https://jsonplaceholder.typicode.com/todos passed on command line
const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, function (error, response, body) {
  let answer = {};
  console.log(typeof answer);
  if (!error) {
    for (const e of JSON.parse(body)) {
      if (e.completed === true) {
        if (!answer.hasOwnProperty(e.userId)) {
          answer[e.userId] = 1;
        } else {
          answer[e.userId] += 1;
        }
      }
    }
    console.log(answer);
  }
});
