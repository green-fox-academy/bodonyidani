'use strict';

var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'todo'
});

connection.connect();

function addTodo(attributes) {
  connection.query('INSERT INTO todo SET ?', attributes, function(err, result) {
    if (err) throw err;
  });
}

function deleteTodo(attributes) {
  connection.query('DELETE FROM todo WHERE ?', attributes, function(err, result) {
    if (err) throw err;
  });
}

function getAllTodos(cb) {
  connection.query('SELECT * FROM todo', function(err, result) {
    if (err) throw err;
    cb(result);
  });
}

function updateTodo(attributes) {
  connection.query('UPDATE todo SET text=? WHERE todo_id=?', [attributes.text, attributes.id], function(err, result) {
    if (err) throw err;
  });
}

module.exports = {
  add: addTodo,
  delete: deleteTodo,
  all: getAllTodos,
  update: updateTodo
};
