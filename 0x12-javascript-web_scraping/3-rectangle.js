#!/usr/bin/node
exports.Rectangle = function (w, h) {
  if ((w > 0) && (h > 0)) {
    this.width = w;
    this.height = h;
  }
};

exports.Rectangle.prototype.print = function () {
  for (let i = 0; i < this.height; i += 1) {
    console.log('X'.repeat(this.width));
  }
};
