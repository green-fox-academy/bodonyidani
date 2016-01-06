'use strict';

var kids = [
  {name: 'Tibbor', candies: 2},
  {name: 'Jozsi', candies: 3},
  {name: 'Agoston', candies: 0},
  {name: 'Julika', candies: 7},
  {name: 'Krisztian', candies: 4}
];

function getRichestKidsName(kids) {
  var richestkid = '';
  var hascandies = 0;
  for (var i = 0; i < kids.length; i++) {
    if (kids[i].candies > hascandies) {
      hascandies = kids[i].candies;
      richestkid = kids[i].name;
    }
  }
  return richestkid;
}

console.log(getRichestKidsName(kids));

function getRichestKidsName2(kids) {
  var richestKid = kids[0];
  kids.forEach(function(currentKid){
    if (currentKid.candies > richestKid.candies) {
      richestKid = currentKid;
    }
  });
  return richestKid.name;
}

console.log(getRichestKidsName2(kids));
