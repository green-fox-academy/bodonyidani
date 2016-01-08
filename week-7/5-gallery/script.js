'use strict';

var images = [
  './img/anup-0.jpg',
  './img/anup-1.jpg',
  './img/anup-2.jpg',
  './img/anup-3.jpg',
  './img/anup-4.jpg',
  './img/anup-5.jpg',
  './img/anup-6.jpg'
];

var leftbutton = document.querySelector('.leftbutton');
var rightbutton = document.querySelector('.rightbutton');
var currentpic = document.querySelector('.currentpic');

var startingIndex = 0;

rightbutton.addEventListener('click', function () {
  if (startingIndex < images.length - 1) {
    currentpic.setAttribute('src', images[startingIndex + 1]);
    startingIndex += 1;
  } else {
    currentpic.setAttribute('src', images[0]);
    startingIndex = 0;
  }
});

leftbutton.addEventListener('click', function () {
  if (startingIndex > 0) {
    currentpic.setAttribute('src', images[startingIndex - 1]);
    startingIndex -= 1;
  } else {
    currentpic.setAttribute('src', images[images.length - 1]);
    startingIndex = images.length - 1;
  }
});

var thumbnailBox = document.querySelector('.thumbnail-box');

function addThumbnailImage(src) {
  var newThumbnail = document.createElement('img');
  newThumbnail.setAttribute('src', src);
  newThumbnail.classList.add('thumbnail-image');
  thumbnailBox.appendChild(newThumbnail);
}

for (var i = 0; i < images.length; i++) {
  addThumbnailImage(images[i]);
}
