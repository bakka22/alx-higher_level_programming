#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const emp = () => {};
const actor = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;
request(url, function (error, response, body) {
  if (error) emp();
  const data = JSON.parse(body);
  for (const film of data.results) {
    const charachters = film.characters;
    if (charachters.includes(actor)) {
      count += 1;
    }
  }
  console.log(count);
});
