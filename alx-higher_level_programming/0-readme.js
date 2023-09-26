#!/usr/bin/node

const fs = require('fs');

// checking if the right number of arguments are taken in
if (process.argv.length !== 3) {
  console.error('Usage: node 0-readme.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the content of the files in utf-8
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    // handle the error
    console.error(error);
  } else {
    // print file's content
    console.log(data);
  }
});
