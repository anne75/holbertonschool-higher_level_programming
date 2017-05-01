#!/usr/bin/node
//read a string (arg 3) and write to a file (arg 2)

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
});
