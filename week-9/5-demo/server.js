'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var items = require('./items.js');

var app = express();

app.use(logRequest);
app.use(express.static('public'));
app.use(bodyParser.json());

app.get('/todos', function (req, res) {
  items.all(function(result) {
    res.json(result);
  });
});

app.post('/todos', function (req, res) {
  var item = items.add(req.body);
  res.status(201).json(item);
});

app.put("/todos/:id", function (req, res) {
  items.update(req.params.id, function(result) {
    res.json(result);
  });
});

app.delete("/todos/:id", function (req, res) {
  items.remove(req.params.id, function(result) {
    res.json(result);
  });
});

app.listen(3000, function () {
  console.log('Listening on port 3000...')
});

function findItem(req, res, found) {
  var id = req.params.id;
  var item = items.get(id, function(result) {
    if (result) {
      found(result);
    } else {
      res.status(404).json({error: "Item not found"})
    }
  });
}

function findItem(req, res, found) {
  var id = req.params.id;
  var item = items.get(id, function(doc) {
    if (doc) {
      found(doc);
    } else {
      res.status(404).json({error: "Item not found"})
    }
  });
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
