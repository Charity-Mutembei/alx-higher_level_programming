#!/usr/bin/node
const firstArgs = process.argv[2];
const secondArgs = process.argv[3];
function add (a, b) {
  if (isNaN(firstArgs) && isNaN(secondArgs)) {
    console.log('NaN');
  } else {
    number1 = parseInt(firstArgs);
    number2 = parseInt(secondArgs);
    addition = (number1 + number2);
    console.log(addition);
  }
}
add();
