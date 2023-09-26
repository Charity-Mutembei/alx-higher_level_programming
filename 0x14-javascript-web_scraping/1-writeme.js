#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file-path> "<string-to-write>"');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file in utf-8
fs.writeFile(filePath, stringToWrite, 'utf-8', (error) => {
  if (error) {
    // Handle the error by printing the error object
    console.error(error);
  }
});
