#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

// Send a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
