#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) throw error;
  fs.writeFile(path, body, { encoding: 'utf8' }, (err) => {
    if (err) throw err;
  });
});
