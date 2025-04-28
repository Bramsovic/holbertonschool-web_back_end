

# Python Async Comprehension

## Description

This project focuses on deepening the understanding of asynchronous generators, async comprehensions, and runtime measurement using Python 3.9.  
It is developed as part of the **Holberton School** curriculum.

---

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep530)
- [Type-hints for generators](https://mypy.readthedocs.io/en/stable/kinds_of_types.html#generators)

---

## Learning Objectives

By the end of this project, you should be able to:

- Write an asynchronous generator in Python.
- Use asynchronous comprehensions.
- Properly annotate generators using type hints.

---

## Requirements

- **Allowed editors**: `vi`, `vim`, `emacs`
- **System**: Ubuntu 20.04 LTS
- **Python Version**: 3.9
- All files must end with a new line.
- The first line of all files must be: `#!/usr/bin/env python3`
- Code must follow [pycodestyle](https://pycodestyle.readthedocs.io/en/latest/) (version 2.5.x).
- Each module must have documentation (docstring).
- Each function/coroutine must have documentation (docstring).
- Documentation must be complete sentences explaining the purpose.
- All functions and coroutines must be type-annotated.

---

## Project Structure

```
holbertonschool-web_back_end/
└── python_async_comprehension/
    ├── 0-async_generator.py
    ├── 1-async_comprehension.py
    ├── 2-measure_runtime.py
    └── README.md
```

---

## Tasks

### 0. Async Generator

**File**: `0-async_generator.py`

Write a coroutine `async_generator` that:

- Loops 10 times.
- Each time, asynchronously waits for 1 second.
- Yields a random number between 0 and 10.

**Example usage**:
```bash
$ ./0-main.py
[4.40, 6.90, 6.29, 4.54, 4.13, 9.99, 6.72, 9.84, 1.00, 1.37]
```

---

### 1. Async Comprehensions

**File**: `1-async_comprehension.py`

Write a coroutine `async_comprehension` that:

- Uses an asynchronous comprehension to collect 10 values from `async_generator`.
- Returns the 10 values as a list.

**Example usage**:
```bash
$ ./1-main.py
[9.86, 8.57, 1.74, 4.07, 0.55, 8.08, 8.38, 1.54, 7.71, 7.67]
```

---

### 2. Run Time for Four Parallel Comprehensions

**File**: `2-measure_runtime.py`

Write a coroutine `measure_runtime` that:

- Executes `async_comprehension` four times in parallel using `asyncio.gather`.
- Measures and returns the total runtime.

> **Note**: The total runtime will be approximately **10 seconds** since all tasks run in parallel, not sequentially.

**Example usage**:
```bash
$ ./2-main.py
10.02
```

---

## Important Notes

- Always use `asyncio.sleep` to perform non-blocking asynchronous waits.
- Use `async for` to correctly iterate over asynchronous generators.
- Proper type annotations are **mandatory** for all functions and coroutines.
- Following the coding standards ensures clean, understandable, and professional-quality code.

---

## Author

👤 **Brahim - Holberton School**

