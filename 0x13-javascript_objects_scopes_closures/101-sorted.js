#!/usr/bin/node

const data = require('./101-data');
const dict = data.dict;

const invertedDict = {};

for (const key in dict) {
  if (dict.hasOwnProperty(key)) {
    const occurrence = dict[key];

    if (!invertedDict[occurrence]) {
      invertedDict[occurrence] = [];
    }

    invertedDict[occurrence].push(key);
  }
}

console.log(invertedDict);
