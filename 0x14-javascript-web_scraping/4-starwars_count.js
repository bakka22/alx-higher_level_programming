#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const actor = '18';
let count = 0;
request(url, function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body);
  for (const film of data.results) {
    const charachters = film.characters;
    for (let i = 0; i < charachters.length; ++i) {
      const character = charachters[i].split('/')[5];
      if (actor === character) {
        count += 1;
      }
    }
  }
  console.log(count);
});
