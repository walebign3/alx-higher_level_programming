#!/usr/bin/node
const fs = require('fs')
let arguments = process.argv
fs.readFile(arguments[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
})
