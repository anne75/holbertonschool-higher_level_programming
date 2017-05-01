#!/usr/bin/node
// concatenate 2 files
// command line arguments are file 1 to start with file 2 to append
// file 3 where to write

const fs = require('fs');

function rw (fromFile, toFile) {
  fs.readFile(fromFile, 'utf8', function (err, data) {
    if (err) {
      return console.log(err);
    }
    fs.appendFile(toFile, data, 'utf8', function (error) {
      if (error) {
        return console.log(error);
      }
    });
  });
}

rw(process.argv[2], process.argv[4]);
rw(process.argv[3], process.argv[4]);
