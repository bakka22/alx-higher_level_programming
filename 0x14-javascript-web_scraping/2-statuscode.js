#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const emp = () => {};
request(url, function (error, response, body) {
  console.log('code:', response.statusCode);
  if (error) emp();
});
