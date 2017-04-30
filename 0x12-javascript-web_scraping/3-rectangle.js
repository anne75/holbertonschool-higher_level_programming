#!/usr/bin/node
// create a prototype Rectangle
// The prototype takes 2 arguments, width and height.

exports.Rectangle = function Rectangle (w, h) {
  if ((w > 0) && (h > 0)) {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let i = 0; i < this.height; i += 1) {
      console.log('X'.repeat(this.width));
    }
  };
};

// exports.Rectangle.prototype.print = function () {
//   for (let i = 0; i < this.height; i += 1) {
//     console.log('X'.repeat(this.width));
//   }
// };
