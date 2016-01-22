'use strict';

function PowerRanger(color) {
  this.color = color;
}

var proto = {isPowerful: true};

PowerRanger.prototype = proto;

var yellowRanger = new PowerRanger('yellow');

console.log(yellowRanger.color);
console.log(yellowRanger.isPowerful);


/*
**************************************
*/

function PowerRanger(color) {
  this.color = color;
}

function Fighter() {
  this.isPowerful = true;
}

PowerRanger.prototype = new Fighter()

var yellowRanger = new PowerRanger('yellow');

console.log(yellowRanger.color);
console.log(yellowRanger.isPowerful);
