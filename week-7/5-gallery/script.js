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
    thumbnailBox.childNodes[parseInt(currentpic.src[currentpic.src.length - 5])].classList.add('active-image');
    startingIndex += 1;
  } else {
    currentpic.setAttribute('src', images[0]);
    thumbnailBox.childNodes[0].classList.add('active-image');
    startingIndex = 0;
  }
});

leftbutton.addEventListener('click', function () {
  if (startingIndex > 0) {
    currentpic.setAttribute('src', images[startingIndex - 1]);
    thumbnailBox.childNodes[parseInt(currentpic.src[currentpic.src.length - 5])].classList.add('active-image');
    startingIndex -= 1;
  } else {
    currentpic.setAttribute('src', images[images.length - 1]);
    thumbnailBox.childNodes[parseInt(currentpic.src[currentpic.src.length - 5])].classList.add('active-image');
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

var thumbnailBox = document.querySelector('.thumbnail-box');

thumbnailBox.addEventListener('click', function() {
  var newSrc = event.target.currentSrc;
  event.target.classList.add('active-image');
  currentpic.setAttribute('src', newSrc);
  startingIndex = parseInt(newSrc[newSrc.length - 5]);
});
