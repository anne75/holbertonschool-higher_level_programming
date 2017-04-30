#!/usr/bin/node
const Rectangle = require('./4-rectangle').Rectangle;

exports.Square = function (size) {
  Rectangle.call(this, size, size);
  this.size = size;
};

exports.Square.prototype = Object.create(Rectangle.prototype);
exports.Square.constructor = exports.Square;
