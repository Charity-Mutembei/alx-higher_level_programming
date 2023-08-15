#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // If w or h is 0 or less, or not a positive integer, create an empty object
      return;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    if (!this.width || !this.height) {
      console.log('Empty Rectangle');
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    if (!this.width || !this.height) {
      return;
    }

    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    if (!this.width || !this.height) {
      return;
    }

    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
