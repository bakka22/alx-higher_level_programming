#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
let characters = [];
const printable = [];
function getChar (actor) {
  return new Promise((resolve, reject) => {
    request(actor, function (err, res, body) {
      if (err) reject(err);
      const name = JSON.parse(body).name;
      printable.push(name);
      resolve(0);
    });
  });
}
function getActors () {
  return new Promise((resolve, reject) => {
    request(url, function (err, res, body) {
      if (err) reject(err);
      characters = JSON.parse(body).characters;
      resolve(0);
    });
  });
}
async function getAll () {
  await getActors();
  for (const actor of characters) {
    await getChar(actor);
  }
  for (const tmp of printable) {
    console.log(tmp);
  }
}
getAll();
