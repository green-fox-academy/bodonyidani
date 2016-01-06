'use strict';

function greet(name) {
  console.log('Csaaa ' + name + '!');
}

greet('Dani');

var koszontes = greet;

koszontes('haver');

var print = console.log;

function greeter(name, log) {
  log('Csovi ' + name);
}

greeter('Lajoskam', print);

var add = function (a, b) {
  return a + b;
}

console.log(add(1, 2));

greeter('Csabi', function(text) {
  console.log(text, 'logged by my function');
});
