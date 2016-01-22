function updateTodo(id, cb) {
  connection.query('UPDATE todo SET completed = \'true\' WHERE id=?', id, function(err, result) {
    if (err) throw err;
    cb(result);
  });
}

app.put('/todos/:id', function (req, res) {
  items.update(req.params.id, function(result) {
    res.json(result);
  });
});
