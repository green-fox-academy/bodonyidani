'use strict';

var candyButton = document.querySelector('.make-candy');
var lollipopButton = document.querySelector('.buy-lollipop');
var candyCounter = document.querySelector('.candies');
var lollipopCounter = document.querySelector('.lollipops');
var speedoMeter = document.querySelector('.speedometer');

var candyCount = 1000;
var lollipopCount = 0;
var currentInterval = 0;
var currentSpeed = 0;
var newInterval = 0;

function displayCandies() {
  candyCounter.innerText = candyCount;
}

function displayLollipops() {
  lollipopCounter.innerText = lollipopCount;
}

function calculateInterval() {
  var interval = currentInterval;
  if (lollipopCount > 0) {
    interval = Math.floor(1000 / lollipopCount * 10);
  }
  return interval;
}

function generateCandies() {
  if (currentInterval > 0) {
    clearInterval(newInterval);
    newInterval = setInterval(function() {
        candyCount += 1;
        displayCandies();
      }, currentInterval);
  } else {
    clearInterval(newInterval);
  }
}

function updateSpeed() {
  currentInterval = calculateInterval();
  currentSpeed = Math.floor(1000 / currentInterval);
  speedoMeter.innerText = currentSpeed;
  generateCandies();
}

candyButton.addEventListener('click', function() {
  candyCount++;
  displayCandies();
});

lollipopButton.addEventListener('click', function() {
  candyCount -= 10;
  displayCandies();
  lollipopCount++;
  displayLollipops();
  if (lollipopCount % 10 === 0) {
    updateSpeed();
  };
});
