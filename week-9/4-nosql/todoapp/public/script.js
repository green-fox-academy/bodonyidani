'use strict';

var url = 'http://localhost:3000/todos';
var backlogContainer = document.querySelector('.backlog-container');
var doneContainer = document.querySelector('.done-container');
var addTaskButton = document.querySelector('.add-task');
var newTask = document.querySelector('.task-input');

function createRequest(method, url, data, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open(method, url);
  probaRequest.setRequestHeader('Content-Type', 'application/json');
  probaRequest.send(data);
  probaRequest.onreadystatechange = function() {
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}

var listCallback = function(response) {
  console.log('response:', response);
  var todoItems = JSON.parse(response);
  todoItems.forEach(function(todoItem) {
    var newTodoDiv = document.createElement('div');
    var newTodoItem = document.createElement('p');
    var newMarkDoneButton = document.createElement('button');
    var newDeleteButton = document.createElement('button');
    newMarkDoneButton.innerHTML = 'Mark Done';
    newMarkDoneButton.classList.add('done-button');
    newMarkDoneButton.setAttribute('id', 'button-' + todoItem._id);
    newDeleteButton.innerHTML = 'Delete';
    newDeleteButton.classList.add('delete-button');
    newDeleteButton.setAttribute('id', 'delete-button-' + todoItem._id);
    newTodoItem.innerText = todoItem.text;
    newTodoDiv.classList.add('todo-item');
    newTodoDiv.setAttribute('id', 'div-' + todoItem._id);
    newTodoItem.classList.add('todo-text');
    if (todoItem.completed === false) {
      backlogContainer.appendChild(newTodoDiv);
      newTodoDiv.appendChild(newTodoItem);
      newTodoDiv.appendChild(newMarkDoneButton);
      newTodoDiv.appendChild(newDeleteButton);
    } else {
      doneContainer.appendChild(newTodoDiv);
      newTodoDiv.appendChild(newTodoItem);
    }
  });
}

var createTodoCallback = function(response) {
  backlogContainer.innerHTML = '';
  doneContainer.innerHTML = '';
  refresh();
}

var changeStatusCallback = function(response) {
  backlogContainer.innerHTML = '';
  doneContainer.innerHTML = '';
  refresh();
}

var deleteTodoCallback = function(response) {
  backlogContainer.innerHTML = '';
  doneContainer.innerHTML = '';
  refresh();
}

addTaskButton.addEventListener('click', function() {
  var newTodo = JSON.stringify({text: newTask.value});
  createRequest('POST', url, newTodo, createTodoCallback);
});

var refresh = function() {
  createRequest('GET', url, {}, listCallback);
}

refresh();

backlogContainer.addEventListener('click', function() {
  if (event.target.classList[0] === 'done-button') {
    var taskidAndName = event.target.parentNode.childNodes[0].innerHTML;
    var taskid = taskidAndName[0];
    var taskName = '';
    for (var i = 2; i < taskidAndName.length; i++) {
      taskName += taskidAndName[i];
      }
    var doneTask = JSON.stringify({_id: taskid, text: taskName, completed: true});
    createRequest('PUT', url + '/' + taskid, doneTask, changeStatusCallback);
  } else if (event.target.classList[0] === 'delete-button') {
      var taskidAndName = event.target.parentNode.childNodes[0].innerHTML;
      var taskid = taskidAndName[0];
      var taskName = '';
      for (var i = 2; i < taskidAndName.length; i++) {
        taskName += taskidAndName[i];
        }
      var doneTask = JSON.stringify({_id: taskid, text: taskName, completed: true, destroyed: true});
      createRequest('DELETE', url + '/' + taskid, doneTask, changeStatusCallback);
  }
});
