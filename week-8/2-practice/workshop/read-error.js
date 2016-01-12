'use strict';

var fs = require('fs');

try {
  var content = fs.readFileSync('korte.text');
} catch (e) {
  content = 'para vaaaan';
}

console.log(String(content));
