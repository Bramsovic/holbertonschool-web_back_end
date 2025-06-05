const express = require('express');
const fs = require('fs').promises;

const app = express();

function countStudents(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      const fields = {};
      for (const line of students) {
        const [firstname, , , field] = line.split(',');
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      }

      let result = `Number of students: ${students.length}`;
      for (const field in fields) {
        if (Object.hasOwn(fields, field)) {
          result += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
        }
      }

      return result;
    });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const path = process.argv[2];

  countStudents(path)
    .then((data) => {
      res.set('Content-Type', 'text/plain');
      res.send(`This is the list of our students\n${data}`);
    })
    .catch(() => {
      res.set('Content-Type', 'text/plain');
      res.send('This is the list of our students\nCannot load the database');
    });
});

app.listen(1245);

module.exports = app;
