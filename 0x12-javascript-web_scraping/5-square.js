#!/usr/bin/node
// create a child prototype Square inheriting from Rectangle
// Square takes in one parameter, size

const Rectangle = require('./4-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}

// Square.prototype = Object.create(Rectangle.prototype);
// Square.constructor = Square;

exports.Square = Square;
