'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'},
]

function filterNamesBySex(kids, sex) {
  var kidsByGender = [];
  kids.forEach(function(kid) {
    if (kid.sex === sex) {
      kidsByGender.push(kid.name);
    }
  });
  return kidsByGender;
}

console.log(filterNamesBySex(kids, 'female'));
