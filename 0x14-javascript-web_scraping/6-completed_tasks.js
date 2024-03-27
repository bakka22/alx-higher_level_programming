#!/usr/bin/node
const request = require('request');
const url = process.argv[2] + '/';
const result = {};
function makeRequest(j) {
  return new Promise((resolve, reject) => {
    request(url + j, function(error, response, body) {
      if (error) {
        reject(error);
      } else {
        const data = JSON.parse(body);
        resolve(data.completed ? 1 : 0);
      }
    });
  });
}
async function countCompleted(min, max) {
  let count = 0;
  for (let j = min; j <= max; j++) {
    count += await makeRequest(j);
  }
  return count;
}
async function res() {
  for (let i = 1; i <= 10; ++i) {
    let count = 0;
    const min = i * 20 - 19;
    const max = i * 20;
    count = await countCompleted(min, max);
    result[i.toString()] = count;
  }
}
res().then(() => console.log(result));
