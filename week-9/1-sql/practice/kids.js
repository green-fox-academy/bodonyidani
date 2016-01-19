'use strict';

var kids = [
  {name: 'Juliska', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'},
]

function getAgeByName(list, name) {
  for (var i = 0; i < list.length; i++) {
    if (list[i]['name'] === name) {
      return list[i]['age'];
    }
  }
}

function getAgeByName2(kids, name) {
  var age = 0;
  kids.forEach(function(kid) {
    if (kid.name === name) {
      age = kid.age;
    }
  });
  return age;
}

function countByAge(kids, age) {
  var count = 0;
  for (var i = 0; i < kids.length; i++) {
    if (kids[i].age === age) {
      count++;
    }
  }
  return count;
}

function countByAge2(kids, age) {
  var count = 0;
  kids.forEach(function(kid) {
    if (kid.age === age) {
      count++;
    }
  });
  return count;
}

function getAges(input) {
  var output = [];
  input.forEach(function(i) {
    output.push(i.age);
  });
  return output;
}

function getAges2(input) {
  var output = [];
  for (var i = 0; i < input.length; i++) {
    output.push(input[i].age);
  }
  return output;
}

function getAges3(kids) {
  return kids.map(function(kid) {
    return kid.age;
  });
}

function getTheLongestNamesAge(kids) {
  var longestName = '';
  var age = 0;
  kids.forEach(function(kid) {
    if (kid.name.length > longestName.length) {
      longestName = kid.name;
      age = kid.age;
    }
  });
  return age;
}




console.log(getAgeByName(kids, 'Gerda')); // 9
console.log(getAgeByName2(kids, 'Gerda'));
console.log(countByAge(kids, 8)); // 2
console.log(countByAge2(kids, 8));
console.log(getAges(kids)); // [8, 7, 6, 9, 8]
console.log(getAges2(kids));
console.log(getAges3(kids));
console.log(getTheLongestNamesAge(kids)); // 8
