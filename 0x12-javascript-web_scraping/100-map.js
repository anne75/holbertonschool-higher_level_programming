#!/usr/bin/node
// use map to make an array from another one
const list = require('./100-data').list;
const result = list.map(function (value, index) {
  return value * index;
}
);
console.log(list);
console.log(result);
