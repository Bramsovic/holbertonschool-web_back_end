# NodeJS Basics

![Node.js Logo](https://nodejs.org/static/images/logo.svg)

This repository contains a series of Node.js exercises and projects designed to help you master the fundamentals of Node.js, including file operations, HTTP servers, Express.js, and more.

## Table of Contents
- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Provided Files](#provided-files)
- [Tasks](#tasks)
  - [0. Executing basic javascript with Node JS](#0-executing-basic-javascript-with-node-js)
  - [1. Using Process stdin](#1-using-process-stdin)
  - [2. Reading a file synchronously with Node JS](#2-reading-a-file-synchronously-with-node-js)
  - [3. Reading a file asynchronously with Node JS](#3-reading-a-file-asynchronously-with-node-js)
  - [4. Create a small HTTP server using Node's HTTP module](#4-create-a-small-http-server-using-nodes-http-module)
  - [5. Create a more complex HTTP server using Node's HTTP module](#5-create-a-more-complex-http-server-using-nodes-http-module)
  - [6. Create a small HTTP server using Express](#6-create-a-small-http-server-using-express)
  - [7. Create a more complex HTTP server using Express](#7-create-a-more-complex-http-server-using-express)
  - [8. Organize a complex HTTP server using Express](#8-organize-a-complex-http-server-using-express)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Author](#author)
- [License](#license)

## Description
This project is part of the Holberton School curriculum and focuses on Node.js basics. It covers various aspects of Node.js development including file system operations, process handling, HTTP servers, and Express.js framework.

## Learning Objectives
By completing this project, you will be able to:
- Run JavaScript using Node.js
- Use Node.js modules
- Read files using Node.js
- Access command line arguments and environment variables
- Create HTTP servers with Node.js and Express.js
- Implement advanced routes with Express.js
- Use ES6 with Node.js via Babel
- Develop faster using Nodemon

## Requirements
- Allowed editors: vi, vim, emacs, Visual Studio Code
- Files interpreted/compiled on Ubuntu 20.04 LTS using Node.js (version 20.x.x)
- All files must end with a new line
- Code must use `.js` extension
- Code must pass all tests and lint checks
- ESLint configuration provided must be used
- All functions/classes must be exported using `module.exports = myFunction;`

## Provided Files
- `database.csv`: Sample student database
- `package.json`: Project configuration and dependencies
- `babel.config.js`: Babel configuration
- `.eslintrc.js`: ESLint configuration

## Tasks

### 0. Executing basic javascript with Node JS
**File:** `0-console.js`  
Create a function that prints to STDOUT.

### 1. Using Process stdin
**File:** `1-stdin.js`  
Create an interactive program that reads user input.

### 2. Reading a file synchronously with Node JS
**File:** `2-read_file.js`  
Read and process a CSV file synchronously.

### 3. Reading a file asynchronously with Node JS
**File:** `3-read_file_async.js`  
Read and process a CSV file asynchronously using Promises.

### 4. Create a small HTTP server using Node's HTTP module
**File:** `4-http.js`  
Create a basic HTTP server that responds with a simple message.

### 5. Create a more complex HTTP server using Node's HTTP module
**File:** `5-http.js`  
Create an HTTP server with multiple endpoints, including student data.

### 6. Create a small HTTP server using Express
**File:** `6-http_express.js`  
Create a basic Express server.

### 7. Create a more complex HTTP server using Express
**File:** `7-http_express.js`  
Create an Express server with student data endpoints.

### 8. Organize a complex HTTP server using Express
**Directory:** `full_server/`  
Create a well-organized Express server with controllers and routes.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/holbertonschool-web_back_end.git
   cd Node_JS_basic
   ```
2. Install dependencies:
   ```bash
   npm install
   ```

## Usage
- Run individual task files:
  ```bash
  node path/to/file.js
  ```
- For development with Nodemon:
  ```bash
  npm run dev
  ```

## Testing
- Run all tests:
  ```bash
  npm run full-test
  ```
- Run only unit tests:
  ```bash
  npm run test
  ```
- Run lint checks:
  ```bash
  npm run check-lint
  ```