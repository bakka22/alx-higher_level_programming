#!/usr/bin/node
const argv = require('node:process').argv;
if (argv.length === 2) {
  console.log('No arguments');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}