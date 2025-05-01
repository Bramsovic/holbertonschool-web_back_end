
# 📦 NoSQL with MongoDB & Python

> A hands-on introduction to NoSQL concepts using MongoDB and Python.  
> Learn how to perform CRUD operations, write efficient queries, and analyze logs using real-world data.

---

## 📚 Table of Contents

- [🚀 About the Project](#-about-the-project)
- [🎯 Learning Objectives](#-learning-objectives)
- [🛠️ Installation](#️-installation)
- [⚙️ Requirements](#️-requirements)
- [📁 Project Structure](#-project-structure)
- [📌 Usage](#-usage)
- [✨ Features](#-features)
- [🧪 Examples](#-examples)
- [🐞 Troubleshooting](#-troubleshooting)
- [👥 Contributors](#-contributors)
- [📝 License](#-license)

---

## 🚀 About the Project

This project is a practical exploration of **NoSQL databases**, particularly **MongoDB**, using both shell scripts and Python scripts with the `PyMongo` driver.

You’ll learn how to:
- Create and manipulate MongoDB databases and collections.
- Perform standard CRUD operations.
- Run queries and aggregations.
- Work with logs and analytics.
- Write modular, clean, and documented Python code.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following without Google:

- What is NoSQL and how it differs from SQL
- The concept of ACID in databases
- Types of NoSQL databases (document, key-value, column, graph)
- Advantages of NoSQL databases
- How document storage works in MongoDB
- How to query, insert, update, and delete documents
- How to use MongoDB from the command line and Python

---

## 🛠️ Installation

### MongoDB (v4.4)

```bash
# For Ubuntu 20.04
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt update
sudo apt install -y mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod
```

### Python 3 & PyMongo

```bash
sudo apt install -y python3 python3-pip
pip3 install pymongo==4.8.0
```

---

## ⚙️ Requirements

- ✅ Ubuntu 20.04 LTS
- ✅ MongoDB v4.4
- ✅ Python 3.9
- ✅ PyMongo 4.8.0
- ✅ Scripts follow `pycodestyle` (2.5.\*)
- ✅ All files end with a newline and have a proper shebang or comment header
- ✅ Python files must be import-safe (`if __name__ == "__main__":`)
- ✅ All modules and functions must have documentation

---

## 📁 Project Structure

```
NoSQL/
├── 0-list_databases
├── 1-use_or_create_database
├── 2-insert
├── 3-all
├── 4-match
├── 5-count
├── 6-update
├── 7-delete
├── 8-all.py
├── 9-insert_school.py
├── 10-update_topics.py
├── 11-schools_by_topic.py
├── 12-log_stats.py
├── *.py (main scripts)
└── README.md
```

---

## 📌 Usage

### 🐚 MongoDB Shell Scripts

```bash
cat 0-list_databases | mongo
cat 2-insert | mongo my_db
```

### 🐍 Python Scripts

```bash
chmod +x 8-main.py
./8-main.py
./12-log_stats.py
```

---

## ✨ Features

- 🧱 Create and select MongoDB databases
- 📝 Insert and retrieve documents
- 🔎 Query by specific fields
- ✏️ Update document fields
- ❌ Delete matched documents
- 🐍 Python wrappers for MongoDB operations using `pymongo`
- 📊 Log analysis for Nginx access logs

---

## 🧪 Examples

### Insert Document (Shell)

```bash
cat 2-insert | mongo my_db
```

### List All Schools (Python)

```python
from pymongo import MongoClient
from 8-all import list_all

client = MongoClient()
collection = client.my_db.school
print(list_all(collection))
```

### Log Stats

```bash
$ ./12-log_stats.py
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
```

---

## 🐞 Troubleshooting

- **MongoDB service not running?**

  ```bash
  sudo systemctl start mongod
  ```

- **Permission denied for Python script?**

  ```bash
  chmod +x script.py
  ```

- **Style issues?**

  ```bash
  pycodestyle file.py
  ```

---

## 👥 Contributors

- 💻 Project by Holberton School students  
---

## 📝 License

This project is part of the Holberton School curriculum. Educational use only.

---
