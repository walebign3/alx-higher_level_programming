#!/usr/bin/node

const fs = require('fs'), request = require('request');

let fileStream = fs.createWriteStream(process.argv[3], 'utf-8');
request(process.argv[2]).pipe(fileStream);
