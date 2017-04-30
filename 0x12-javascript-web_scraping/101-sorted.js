#!/usr/bin/node
// import a dict, reverses keys and values
const dict = require('./101-data').dict;
let answer = {};
for (let k in dict) {
  if (!answer.hasOwnProperty(dict[k])) {
    answer[dict[k]] = [k];
  } else {
    answer[dict[k]].push(k);
  }
}
console.log(answer);
