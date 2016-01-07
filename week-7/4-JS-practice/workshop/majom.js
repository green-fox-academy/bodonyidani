'use strict';

console.log('mukodik');

var cim = document.querySelector('.majom');
console.log(cim);

cim.classList.add('piros');

var majomKep = document.querySelector('img');

majomKep.setAttribute('src', 'https://files.slack.com/files-pri/T0E3ZD06M-F0HKDD6BY/slack_for_ios_upload.jpg')

var bodyvaltozoban = document.querySelector('body');

function kepcsinalo(src) {
  var ujkep = document.createElement('img');
  ujkep.setAttribute('src', src);
  bodyvaltozoban.appendChild(ujkep);
}

var kepek = [
  'http://www.sisense.com/wp-content/uploads/dilbert-bigdata.jpg',
  'http://www.underconsideration.com/brandnew/archives/inbrief_dilbert_nuts.gif',
  'https://files.slack.com/files-pri/T0E3ZD06M-F0HTBEV17/image.jpg',
  'http://hr.sparkhire.com/wp-content/uploads/2013/06/Decoding-Dilbert-6.png',
  'http://cdn3.thr.com/sites/default/files/imagecache/300_portrait/2011/04/dilbert-2011-a-p.jpg'
]

for (var i = 0; i < 5; i++) {
  kepcsinalo(kepek[i]);
}

var gomb = document.querySelector('.csinal');

gomb.addEventListener('click', function() {
  alert('kattintottam!');
  kepcsinalo('http://i1.wp.com/better-operations.com/wp-content/uploads/2015/02/Dilbert-lean-TQM-Six-Sigma-10.gif?resize=640%2C189');
});

window.addEventListener('scroll', function () {
  console.log('scroll baby scroll');
});

var cicagomb = document.querySelector('.cicat');
var kutyagomb = document.querySelector('.kutyat');
var valtoskep = document.querySelector('.cicakutyakep');

kutyagomb.addEventListener('click', function () {
  valtoskep.setAttribute('src', 'http://adogsplanet.com/wp-content/uploads/2014/08/khjgcvmjhgjg.jpg');
});

cicagomb.addEventListener('click', function () {
  valtoskep.setAttribute('src', 'http://i2.kym-cdn.com/photos/images/facebook/000/848/659/40f.jpg');
});
