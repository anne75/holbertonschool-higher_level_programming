#!/usr/bin/node
const n = parseInt(process.argv[2], 10);
function fact (a) {
  if (isNaN(a) || (a === 0)) {
    return 1;
  }
  return a * fact(a - 1);
}
console.log(fact(n));
