'use strict';

var fs = require('fs');

var content = (fs.readFileSync('alma.txt'));

console.log(content.toString());
console.log(String(content));
console.log('end!');
