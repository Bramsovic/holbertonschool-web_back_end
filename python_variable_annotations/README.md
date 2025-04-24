
# 🧠 Python - Variable Annotations

Welcome to this project dedicated to mastering **type annotations in Python 3**! 🐍  
This project will guide you through the core concepts of annotating variables and functions, using **MyPy** for validation, and understanding **duck typing** in a Pythonic way.

---

## 📚 Resources

- 📄 [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- 🧾 [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

---

## 🎯 Learning Objectives

By the end of this project, you will be able to explain:

- 🏷️ What type annotations are in Python
- ✍️ How to annotate **function signatures** and **variables**
- 🦆 The concept of **duck typing**
- ✅ How to validate code using **MyPy**

---

## ✅ Requirements

- **Interpreter:** Python 3.9 on Ubuntu 20.04 LTS  
- **Allowed editors:** `vi`, `vim`, `emacs`  
- **Code style:** `pycodestyle` version 2.5  
- **Execution rules:**
  - Each file must begin with:
    ```python
    #!/usr/bin/env python3
    ```
  - All files must be **executable**
  - All files must **end with a new line**
  - Include **docstrings** for all modules, classes, and functions

---

## 📂 Project Structure

```plaintext
python_variable_annotations/
├── 0-add.py                 # Add two floats
├── 1-concat.py              # Concatenate two strings
├── 2-floor.py               # Floor of a float
├── 3-to_str.py              # Float to string
├── 4-define_variables.py    # Define annotated variables
├── 5-sum_list.py            # Sum a list of floats
├── 6-sum_mixed_list.py      # Sum a list of ints and floats
├── 7-to_kv.py               # Return tuple of string and squared number
├── 8-make_multiplier.py     # Return a function that multiplies
├── 9-element_length.py      # Duck-typed function with Iterable
└── README.md                # You’re here!
```
## 🧪 Task Overview

Each task in this project builds your understanding of type annotations in Python. Here's a breakdown:

```plaintext
| 🔢 Task | 📌 Title          | 🧠 Description                                                                         | 📁 File                  |
|--------|--------------------|----------------------------------------------------------------------------------------|--------------------------|
| 0️⃣     | `add`              | Write a function that adds two `float` numbers and returns a `float`.                | `0-add.py`               |
| 1️⃣     | `concat`           | Create a function that concatenates two `str` strings and returns the result.        | `1-concat.py`            |
| 2️⃣     | `floor`            | Implement a function that takes a `float` and returns its floor value as an `int`.   | `2-floor.py`             |
| 3️⃣     | `to_str`           | Write a function to convert a `float` to a `str`.                                    | `3-to_str.py`            |
| 4️⃣     | `define_variables` | Define and annotate variables: `int`, `float`, `bool`, and `str`.                    | `4-define_variables.py`  |
| 5️⃣     | `sum_list`         | Build a function that sums a list of `float`s and returns a `float`.                 | `5-sum_list.py`          |
| 6️⃣     | `sum_mixed_list`   | Write a function that sums a list of `int`s and `float`s, returning a `float`.       | `6-sum_mixed_list.py`    |
| 7️⃣     | `to_kv`            | Create a function returning a `Tuple[str, float]`, where the number is squared.      | `7-to_kv.py`             |
| 8️⃣     | `make_multiplier`  | Write a higher-order function that returns a multiplier `Callable`.                  | `8-make_multiplier.py`   |
| 9️⃣     | `element_length`   | Use duck typing to annotate a function returning lengths of iterable elements.       | `9-element_length.py`    |

```

## 🚀 Running the Code

To execute a script:
```bash
chmod +x 0-add.py
./0-add.py
```

To check type correctness using MyPy:
```bash
mypy --strict 0-add.py
```

---

## 🤝 Contributing

Want to contribute? Follow these steps:

1. Fork the repository  
2. Create a new branch: `git checkout -b new-feature`  
3. Commit your changes: `git commit -m "Add feature"`  
4. Push to your branch: `git push origin new-feature`  
5. Open a Pull Request 🚀

---

## 👨‍💻 Author

Part of the Holberton School Web Back-End curriculum  
📁 Repository: [holbertonschool-web_back_end](https://github.com/holbertonschool-web_back_end)

---

🎉 Happy typing with Python!
```
