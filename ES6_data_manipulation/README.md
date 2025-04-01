# ES6 Data Manipulation

## 📚 Description

This project aims to solidify your understanding of core ES6 features, focusing on efficient data manipulation. You'll learn how to use powerful built-in methods and structures including:

- `map`, `filter`, `reduce`
- Typed Arrays
- `Set`, `Map`, and `WeakMap` data structures

---

## 🎯 Learning Objectives

By the end of this project, you should be able to confidently explain:

- How to use `map`, `filter`, and `reduce` on arrays
- What typed arrays are and how to use them
- The purpose and usage of `Set`, `Map`, and `WeakMap`

---

## 🛠️ Requirements

- Node.js `v20.x.x` and npm `v9.x.x`
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files must end with a new line
- Files must use the `.js` extension
- Tests are run using `Jest`
- Linting with `ESLint`
- Must pass all linting and tests using `npm run full-test`
- All functions must be exported

---

## ⚙️ Setup Instructions

### Install NodeJS 20.x

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

Verify installations:

```bash
node -v
npm -v
```

### Install Project Dependencies

```bash
npm install
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

---

## 🧪 Testing & Linting

- Run tests: `npm run test`
- Run full checks: `npm run full-test`

---

## 📁 Project Structure

Each file implements a specific function using modern ES6 techniques:

| File | Description |
|------|-------------|
| `0-get_list_students.js` | Create a basic list of students |
| `1-get_list_student_ids.js` | Map over students to extract IDs |
| `2-get_students_by_loc.js` | Filter students by location |
| `3-get_ids_sum.js` | Reduce to sum student IDs |
| `4-update_grade_by_city.js` | Filter and map to update grades |
| `5-typed_arrays.js` | Use TypedArray and DataView |
| `6-set.js` | Create a Set from an array |
| `7-has_array_values.js` | Check values existence in a Set |
| `8-clean_set.js` | Filter Set values by prefix |
| `9-groceries_list.js` | Return a Map of grocery items |
| `10-update_uniq_items.js` | Update unique items in a Map |

---

## ✅ Example Output

```js
[
  { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
  { id: 2, firstName: 'James', location: 'Columbia' },
  { id: 5, firstName: 'Serena', location: 'San Francisco' }
]
```

---

## 📎 Resources

Make sure to review:

- [MDN: Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)
- [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
