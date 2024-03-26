#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const emp = () => {};
request(url, function (error, response, body) {
  const data = JSON.parse(body);
  console.log(data.title);
  if (error) emp();
});
