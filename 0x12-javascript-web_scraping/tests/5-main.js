#!/usr/bin/node
const Square = require('../5-square').Square;

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

console.log('0 square');
const s2 = new Square(0);
s2.print();
s2.double();
console.log('double');
s2.print();
