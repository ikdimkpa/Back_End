#!/usr/bin/node
const { dict } = require('./101-data.js');

const sorted_object = {};
let val;
for (const key in dict) {
  val = dict[key];
  if (sorted_object[val] === undefined) {
    sorted_object[val] = [];
    sorted_object[val].push(key);
  } else {
    sorted_object[val].push(key);
  }
}
console.log(sorted_object);
