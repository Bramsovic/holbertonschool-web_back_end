# ES6 Classes

## 📚 Description

This project is focused on Object-Oriented Programming (OOP) using JavaScript ES6. You'll explore how to define and use classes, create methods (including static ones), implement inheritance, and dive into metaprogramming with symbols. The project emphasizes clean code practices using ESLint and robust testing via Jest.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following without external help:

- ✅ How to define a class
- ✅ How to add methods to a class
- ✅ Why and how to use static methods
- ✅ How to extend a class from another
- ✅ Metaprogramming and symbols

---

## ⚙️ Requirements

- Ubuntu 20.04 LTS
- Node.js v20.x.x
- npm v9.x.x or higher
- All code files should end with a new line
- Only `.js` files are allowed
- Testing with **Jest**
- Linting with **ESLint**
- All tests and linter checks must pass using `npm run full-test`

---

## 🛠️ Setup Instructions

### 1. Install Node.js

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

### 2. Verify Installation

```bash
node -v   # Should output v20.15.1
npm -v    # Should output 10.7.0
```

### 3. Install Project Dependencies

Inside your project folder, run:

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

### 4. Install from `package.json`

If a `package.json` is already present:

```bash
npm install
```

---

## 📁 Configuration Files

### `package.json`

```json
{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  }
}
```

### `babel.config.js`

```js
module.exports = {
  presets: [['@babel/preset-env', { targets: { node: 'current' } }]],
};
```

### `.eslintrc.js`

```js
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: ['airbnb-base', 'plugin:jest/all'],
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': ['error', 'LabeledStatement', 'WithStatement'],
  },
};
```

---

## 🚀 Usage

- Run a JavaScript file:  
  ```bash
  npm run dev filename.js
  ```

- Run the linter:  
  ```bash
  npm run check-lint
  ```

- Run tests with Jest:  
  ```bash
  npm test
  ```

- Run both linter and tests:  
  ```bash
  npm run full-test
  ```

---

## 🧩 Key Tasks

- `0-classroom.js`: Create a basic `ClassRoom` class
- `1-make_classrooms.js`: Generate an array of `ClassRoom` instances
- `2-hbtn_course.js`: Build `HolbertonCourse` with type validation and accessors
- `3-currency.js`: Implement a `Currency` class with display formatting
- `4-pricing.js`: Create `Pricing` with static method `convertPrice`
- `5-building.js`: Abstract class `Building` with method contract enforcement
- `6-sky_high.js`: Extend `Building` in `SkyHighBuilding` with custom messaging
- `7-airport.js`: Create an `Airport` class with string representation
- `8-hbtn_class.js`: Customize behavior with type casting (`Number`, `String`)
- `9-hoisting.js`: Resolve class hoisting and fix instantiation issues
- `10-car.js`: Use symbols to implement `cloneCar` method with ES6 metaprogramming

---

## 📦 Repository

**GitHub Repository:** `holbertonschool-web_back_end`  
**Project Directory:** `ES6_classes`

---

Happy coding! 🚀
