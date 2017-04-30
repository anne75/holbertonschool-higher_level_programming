#!/usr/bin/node
const Sq = require('./5-square').Square;

exports.Square = function (size) {
  Sq.call(this, size);
};

exports.Square.prototype = Object.create(exports.Square.prototype);
exports.Square.constructor = exports.Square;

exports.Square.prototype.charPrint = function (c = 'X') {
  for (let i = 0; i < this.size; i += 1) {
    console.log(c.repeat(this.size));
  }
};
