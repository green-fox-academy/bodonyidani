'use strict';

var images = [
  './img/Dilbert_1.gif',
  './img/Dilbert_2.gif',
  './img/Dilbert_3.gif',
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
