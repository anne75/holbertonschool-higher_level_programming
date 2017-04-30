#!/usr/bin/node
const Rectangle = require('../3-rectangle').Rectangle;

const r1 = new Rectangle(2, 3);
// console.log('2, 3');
r1.print();

const r2 = new Rectangle(10, 5);
// console.log('10, 5')
// console.log('----------');
r2.print();

const r3 = new Rectangle(10, 1);
// console.log('10, 1');
r3.print();
