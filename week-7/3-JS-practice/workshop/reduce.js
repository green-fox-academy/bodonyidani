'use strict';

var numbers = [5, 6, 3, 9];

var sum = numbers.reduce(function(acc, i) {
  return acc + i;
}, 0);

console.log(sum);
