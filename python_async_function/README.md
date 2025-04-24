# 🌀 Python Async Functions

This project is part of the Holberton School curriculum and introduces asynchronous programming in Python using `async` and `await` with `asyncio`. It provides hands-on experience with writing coroutines, scheduling them, measuring execution time, and managing tasks concurrently.

---

## 📚 Resources

Make sure to review these before starting the tasks:

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to:

- Understand the `async` and `await` syntax in Python.
- Execute an asynchronous program using `asyncio`.
- Create and run concurrent coroutines.
- Use `asyncio.Task` to manage asynchronous execution.
- Integrate the `random` module for realistic delay simulation.
- Type-annotate coroutines and functions for better code clarity.

---

## ✅ Requirements

- Python 3.9, executed on Ubuntu 20.04 LTS
- All files must start with:
  ```python
  #!/usr/bin/env python3
  ```
- Code must follow `pycodestyle` (version 2.5.x)
- Type annotations are **mandatory** for all functions and coroutines.
- Every module, function, and class must include **complete docstrings**
- All files should be executable and end with a new line

---

## 🧪 Task Overview


```
| 🔢 Task | 📌 Title           | 🧠 Description                                                                 | 📁 File                      
|------------------------------------------------------------------------------------------------------------------------------------------------|
| 0️⃣     | `wait_random`       | Coroutine that returns a random delay between 0 and `max_delay`.                | `0-basic_async_syntax.py`    |
| 1️⃣     | `wait_n`            | Spawns `n` concurrent coroutines using `wait_random` and returns sorted delays. | `1-concurrent_coroutines.py` |
| 2️⃣     | `measure_time`      | Measures the runtime of `wait_n` and returns average delay.                     | `2-measure_runtime.py`       |
| 3️⃣     | `task_wait_random`  | Wraps `wait_random` into an `asyncio.Task` for task-based execution.            | `3-tasks.py`                 |
| 4️⃣     | `task_wait_n`       | Uses tasks instead of coroutines to schedule concurrent executions.             | `4-tasks.py`                 |
```

---

## 🚀 Run & Test

Example:

```bash
chmod +x 0-main.py
./0-main.py
```

Or run with Python:

```bash
python3 0-main.py
```

Use `asyncio.run()` to execute any async function from your main scripts.

---

## 📦 Repository Structure

```
python_async_function/
├── 0-basic_async_syntax.py
├── 1-concurrent_coroutines.py
├── 2-measure_runtime.py
├── 3-tasks.py
├── 4-tasks.py
├── 0-main.py
├── 1-main.py
├── ...
└── README.md
```

---

## 👨‍💻 Author

Project from **Holberton School – Web Back End specialization**.
