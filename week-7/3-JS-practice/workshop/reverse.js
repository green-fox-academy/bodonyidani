'use strict';

function reverse(string) {
  var output = '';
  for (var i = string.length - 1; i >= 0; i--) {
    output += string[i];
  };
  console.log(output);
}

reverse('majom');

// recursive

function reverse2(input) {
  return reverseRecursive(input, input.length - 1);
}

function reverseRecursive(input, i) {
  if (i < 0) {
    return '';
  } else {
    return input[i] + reverseRecursive(input, i - 1);
  }
}

console.log(reverse2('kacsa'));
