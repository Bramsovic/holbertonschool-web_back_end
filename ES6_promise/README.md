# ES6 Promises

> Learn how to handle asynchronous JavaScript operations using Promises, async/await, and error handling mechanisms.  
---

## 📚 Description

This project deep-dives into handling asynchronous operations in JavaScript using modern ES6+ constructs. You will learn how Promises work, how to chain them, handle multiple asynchronous tasks, and integrate error handling with try/catch and async/await.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain and use:

- JavaScript Promises (what, how, and why)
- `then`, `resolve`, `catch` methods
- Every method of the `Promise` object
- Error handling with `throw` and `try/catch`
- The `await` operator
- Asynchronous functions with `async`

---

## 🛠️ Requirements

- Ubuntu 20.04 LTS
- Node.js `v20.x.x` and npm `v9.x.x`
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- Files must:
  - Use `.js` extension
  - End with a new line
  - Export all functions
- Testing: Jest (`npm run test`)
- Linting: ESLint
- Must pass all tests and lint via `npm run full-test`

---

## ⚙️ Setup Instructions

### Install Node.js 20.x

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

### Verify Installation

```bash
node -v   # Should be v20.x.x
npm -v    # Should be v9.x.x
```

### Install Dependencies

```bash
npm install
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
npm install --save-dev eslint
```

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `0-promise.js` | Basic promise creation |
| `1-promise.js` | Resolving or rejecting a promise based on a boolean |
| `2-then.js` | Handling promise resolution and rejection with logging |
| `3-all.js` | Handling multiple successful promises using `Promise.all` |
| `4-user-promise.js` | Returning resolved user signup data |
| `5-photo-reject.js` | Rejected promise simulating file error |
| `6-final-user.js` | Handling multiple promise results (allSettled pattern) |
| `7-load_balancer.js` | Returning the result of the first settled promise |
| `8-try.js` | Simple division with error throwing |
| `9-try.js` | Guardrail function with try/catch and status queuing |

---

## 📦 Utilities

- `utils.js`:
  - `uploadPhoto()` returns:
    ```json
    { "status": 200, "body": "photo-profile-1" }
    ```
  - `createUser()` returns:
    ```json
    { "firstName": "Guillaume", "lastName": "Salva" }
    ```

---

## 🧪 Example Output

```js
Promise { { status: 200, body: 'Success' } }
// OR
Promise { <rejected> Error: The fake API is not working currently }
```

---

## 📎 Resources

Recommended reading:

- [MDN: Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promises: An Introduction](https://developers.google.com/web/fundamentals/primers/promises)
- [Async & Await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await)
- [Try / Catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)

---
