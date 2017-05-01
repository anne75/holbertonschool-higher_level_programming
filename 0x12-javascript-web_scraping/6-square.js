#!/usr/bin/node
const Sq = require('./5-square').Square;

function Square (size) {
  Sq.call(this, size);
}

Square.prototype = Object.create(Sq.prototype);
Square.constructor = Square;

Square.prototype.charPrint = function (c = 'X') {
  for (let i = 0; i < this.height; i += 1) {
    console.log(c.repeat(this.width));
  }
};

exports.Square = Square;
