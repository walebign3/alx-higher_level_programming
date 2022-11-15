#!/usr/bin/node

const fs = require('fs');
const arguments = process.argv;

fs.readFile(arguments[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
