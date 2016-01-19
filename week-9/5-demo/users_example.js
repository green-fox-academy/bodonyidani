var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'testuser',
  password: 'testuser',
  database: 'todo'
});

connection.connect();

function addTodo(attributes) {
  connection.query('INSERT INTO user SET ?', attributes, function(err, result) {
    if (err) throw err;
  });
}

module.exports = {
  add: addTodo
};
