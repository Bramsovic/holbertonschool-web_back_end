# 📚 Python Pagination Project

This project explores how to efficiently paginate large datasets using Python, simulating real-world scenarios like REST APIs with pagination and deletion resilience.

---

## 🧠 Learning Objectives

By the end of this project, you should be able to:

- Implement basic pagination logic using `page` and `page_size`.
- Build hypermedia-style pagination metadata.
- Handle pagination even when dataset entries are deleted (deletion-resilient pagination).
- Use Python features such as:
  - Type annotations
  - `assert` for input validation
  - `math` module for pagination calculations
  - File I/O with `csv.reader`
  - Dict and list manipulations

---

## 📖 Resources

- [REST API Design: Pagination](https://www.restapitutorial.com/lessons/pagination.html)
- [HATEOAS (Hypermedia as the Engine of Application State)](https://en.wikipedia.org/wiki/HATEOAS)

---

## ⚙️ Requirements

- Python 3.9
- Ubuntu 20.04 LTS
- `pycodestyle` compliant code (v2.5.\*)
- `#!/usr/bin/env python3` on first line of all scripts
- All functions and modules must be documented
- Type-annotations are required

---

## 📂 Dataset

The project uses the `Popular_Baby_Names.csv` file as its data source. Ensure it's present at the root of the project.

---

## 🧪 Task Overview

### 0️⃣ `index_range`
- 📁 **File:** `0-simple_helper_function.py`
- 🧠 **Description:** Returns the start and end index for pagination based on page and page_size.

---

### 1️⃣ `get_page`
- 📁 **File:** `1-simple_pagination.py`
- 🧠 **Description:** Returns a page of data from the dataset with input validation using `assert`.

---

### 2️⃣ `get_hyper`
- 📁 **File:** `2-hypermedia_pagination.py`
- 🧠 **Description:** Returns paginated data wrapped with metadata including:
  - `page`
  - `page_size`
  - `next_page`
  - `prev_page`
  - `total_pages`

---

### 3️⃣ `get_hyper_index`
- 📁 **File:** `3-hypermedia_del_pagination.py`
- 🧠 **Description:** Provides deletion-resilient pagination by:
  - Indexing dataset entries
  - Ensuring consistent page navigation even if rows are removed between requests

---


## ✅ Example Outputs

```bash
python3 0-main.py
# (0, 7)
# (30, 45)

python3 1-main.py
# [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ...]
# []

python3 2-main.py
# {
#   'page_size': 2,
#   'page': 1,
#   'data': [...],
#   'next_page': 2,
#   'prev_page': None,
#   'total_pages': 9709
# }

python3 3-main.py
# Handles deleted entries without breaking pagination
```

---

## 🧠 Author

This project is part of the **Holberton School Web Back-End curriculum** and was designed to introduce core concepts of efficient pagination.

---
