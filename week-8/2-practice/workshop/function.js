/*

'use strict';

var button = document.querySelector('button');

button.addEventListener('click', function () {
  shout('kacsa');
});

function shout(word) {
  console.log('AJJJAJAJAJAJ');
  console.log('AJJJAJAJAJAJ');
  console.log('AJJJAJAJAJAJ', word);
  console.log('AJJJAJAJAJAJ');
  console.log('AJJJAJAJAJAJ');
  console.log('AJJJAJAJAJAJ');
}

*/

var human = {
  word: ['kacsa', 'macska', 'mamlasz'],
  name: 'Tibike',
  speak: speak
}

function speak() {
  var _this = this;
  this.word.forEach(function(w) {
    console.log('I am ' + _this.name);
    console.log('Bla-bla-bla ' + w);
  });
}


human.speak();
