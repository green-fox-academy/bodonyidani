'use strict';

var fs = require('fs');

function getFirstIndexInAlmaTxt(letter, cb) {
  fs.readFile('alma.txt', function(err, content) {
    if (err) {
      return cb(err, i);
    }
    var stringContent = String(content);
    for (var i = 0; i < stringContent.length; i++) {
      if (stringContent[i] === letter) {
        return cb(err, i);
      }
    }
  });
}

getFirstIndexInAlmaTxt('l', function(err, index) {
  console.log(index); // -> 3
});
