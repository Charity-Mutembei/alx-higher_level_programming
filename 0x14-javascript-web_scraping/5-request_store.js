#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: node 5-request_store.js <URL> <file-path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Send a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Write the response body to the specified file in utf-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      }
    });
  }
});
