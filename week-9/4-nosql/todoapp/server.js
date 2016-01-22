"use strict"

var express = require("express");
var bodyParser = require("body-parser");
var items = require("./items.js");

var app = express();

// Basic middlewares
app.use(logRequest);
app.use(express.static("public"));
app.use(bodyParser.json());

// GET /todos => list all todo items
app.get("/todos", function (req, res) {
  items.all(function(docs) {
    res.json(docs);
  });
});

app.post("/todos", function (req, res) {
  items.add(req.body, function(doc) {
    res.status(201).json(doc);
  });
});

// GET /todos/1 => gets a single todo item
app.get("/todos/:id", function (req, res) {
  items.all(function(result) {
    res.json(result);
  });
});

// PUT /todos/1 => edit a todo item
// It accepts the same body as the POST /todos request.
app.put("/todos/:id", function (req, res) {
  items.update(req.params.id, function(result) {
    res.json(result);
  });
});

// DELETE /todos/1 => remove a todo item
// It deletes and returns a todo item.
app.delete("/todos/:id", function (req, res) {
  items.remove(req.params.id, function(result) {
    res.json(result);
  });
});

app.listen(3000, function () {
  console.log("Listening on port 3000...")
});

function logRequest(req, res, next) {
  var parts = [
    new Date(),
    req.method,
    req.originalUrl,
  ];
  console.log(parts.join(" "));

  next();
}
