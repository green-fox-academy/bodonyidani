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

function deleteTodo(id, cb) {
  connection.query('DELETE FROM todo WHERE id=?', id, function(err, result) {
    if (err) throw err;
    cb(result);
  });
}

function getItem(id, cb) {
  connection.query('SELECT FROM todo WHERE id=?', id, function(err,result) {
    if (err) throw err;
    cb(result);
  })
}

function getAllTodos(cb) {
  connection.query('SELECT * FROM todo', function(err, result) {
    if (err) throw err;
    cb(result);
  });
}

function updateTodo(id, cb) {
  connection.query('UPDATE todo SET completed = \'true\' WHERE id=?', id, function(err, result) {
    if (err) throw err;
    cb(result);
  });
}

module.exports = {
  add: addTodo,
  remove: deleteTodo,
  get: getItem,
  all: getAllTodos,
  update: updateTodo
};
