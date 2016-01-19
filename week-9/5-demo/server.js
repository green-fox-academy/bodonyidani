'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var items = require('./items.js');

var app = express();

app.use(logRequest);
app.use(express.static('public'));
app.use(bodyParser.json());

app.get('/todos', function (req, res) {
  items.all(function(result){
    res.json(result);
  });
});

app.post('/todos', function (req, res) {
  var item = items.add(req.body);
  res.status(201).json(item);
});

/* GET /todos/1 => gets a single todo item
app.get('/todos/:id', function (req, res) {
  findItem(req, res, function (item) { res.json(item); });
});

// PUT /todos/1 => edit a todo item
// It accepts the same body as the POST /todos request.
app.put('/todos/:id', function (req, res) {
  findItem(req, res, function (item) {
    item.update(req.body);
    res.json(item);
  });
});

app.delete('/todos/:todo_id', function (req, res) {
  findItem(req, res, function (item) {
    items.remove(item.todo_id);
    item.destroyed = true;
    res.json(item);
  });
}); */

app.listen(3000, function () {
  console.log('Listening on port 3000...')
});

function findItem(req, res, found) {
  var id = parseInt(req.params.id);
  var item = items.get(id);
  if (item) {
    found(item);
  } else {
    res.status(404).json({error: 'Item not found'})
  }
}

function logRequest(req, res, next) {
  var parts = [
    new Date(),
    req.method,
    req.originalUrl,
  ];
  console.log(parts.join(' '));

  next();
}
