#!/usr/bin/node
const n = parseInt(process.argv[2], 10);
const m = parseInt(process.argv[3], 10);
function add (a, b) {
  return a + b;
}
console.log(add(m, n));
