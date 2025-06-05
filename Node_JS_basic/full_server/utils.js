import { promises as fs } from 'fs';

export default function readDatabase(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const result = {};

      for (const line of students) {
        const [firstname, , , field] = line.split(',');
        if (!result[field]) result[field] = [];
        result[field].push(firstname);
      }

      return result;
    });
}
