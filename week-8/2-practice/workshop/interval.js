'use strict';

var count = 0;

var interval = setInterval(function() {
  count++;
  console.log('Je-je-jee!', count);
}, 500);

setTimeout(function() {
  console.log('BOOM!');
  clearInterval(interval);
}, 5000);
