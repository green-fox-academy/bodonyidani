'use strict';

function createRequest(url, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open('GET', url);
  probaRequest.send();
  probaRequest.onreadystatechange = function() {
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var todoContainer = document.querySelector('.todo-container');

var todoCallback = function(response) {
  var todoArray = JSON.parse(response);
  todoArray.forEach(function(todoItem) {
    var newTodoItem = document.createElement('p');
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
  });
}

createRequest(url, todoCallback);

function postRequest(url) {
  var testRequest = new XMLHttpRequest();
  testRequest.open('POST', url);
  testRequest.setRequestHeader('Content-Type', 'application/json');
  testRequest.send(JSON.stringify({text: 'Feed Szuperkacsa'}));
}
