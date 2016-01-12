'use strict';

var fs = require('fs');

fs.readFile('korte.text', function(err, content) {
  if (err) {
    console.log('para vaaaan');
  } else {
    console.log(content);
  }
});
