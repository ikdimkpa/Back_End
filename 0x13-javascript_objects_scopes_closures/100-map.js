#!/usr/bin/node
const { list } = require('./100-data.js');

let x = 0;
let value;
const result = list.map((num) => {
  value = x * num;
  x++;
  return value;
});
console.log(list);
console.log(result);
