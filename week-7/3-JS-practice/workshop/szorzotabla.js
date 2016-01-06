'use strict'

function szorzotabla(number) {
  var output = '';
  for (var i = 1; i <= 10; i++) {
    output += i + ' * ' + number + ' = ' + number * i + '\n';
  }
  return output;
}

for (var i = 1; i <= 10; i++) {
  console.log(szorzotabla(i));
}


function recSzorzo(number, i) {
  if (i > 10) {
    return '';
  }
  return i + ' * ' + number + ' = ' + number * i + '\n' + recSzorzo(number, i + 1);
}

console.log(recSzorzo(4, 1));
