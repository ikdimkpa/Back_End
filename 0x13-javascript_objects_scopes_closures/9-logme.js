#!/usr/bin/node
let key =0;

exports.logMe = function (item)
{
	console.log(`${key}: ${item}`);
	key += 1;
}
