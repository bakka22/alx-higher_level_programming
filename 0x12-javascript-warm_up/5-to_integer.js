#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not an number');
} else {
  console.log(parseInt(process.argv[2]));
}
