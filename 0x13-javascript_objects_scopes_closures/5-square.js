#!/usr/bin/node

const Rectangle = require("./2-rectangle");

class Square extends Rectangle {
  constructor (size) {
    super();
    this.size = size;
  }

  // Method that prints the rectangle using the character X.
  print () {
    for (let i = 0; i < this.size; i++) {
      console.log('X'.repeat(this.size));
    }
  }

  // Method that multiples the width and the height of the rectangle by 2.
  double () {
    this.size *= 2;
  }
}

module.exports = Square;
