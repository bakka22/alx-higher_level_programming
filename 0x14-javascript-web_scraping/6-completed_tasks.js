#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const result = {};
request(url, function (err, res, body) {
  if (err) throw err;
  const all = JSON.parse(body);
  for (let i = 0; i < all.length; ++i) {
    const task = all[i];
    if (task.completed && !result[task.userId]) {
      result[task.userId] = 0;
    }
    if (task.completed) ++result[task.userId];
  }
  console.log(result);
});
