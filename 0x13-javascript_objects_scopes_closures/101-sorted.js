#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};

Object.getOwnPropertyNames(dict).forEach(occurrences => {
  if (newDict[dict[occurrences]] === undefined) {
    newDict[dict[occurrences]] = [occurrences];
  } else {
    newDict[dict[occurrences]].push(occurrences);
  }
});

console.log(newDict);
