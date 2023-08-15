#!/usr/bin/node
const args = process.argv[2];
if (isNaN(args)) {
  console.log('Missing size');
} else {
  number = parseInt(args);
  for (let i = 0; i < number; i++) {
    let row = '';
    for (let j = 0; j < number; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
