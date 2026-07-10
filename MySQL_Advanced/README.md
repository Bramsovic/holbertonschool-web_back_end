# MySQL Advanced

This project covers advanced MySQL concepts such as constraints, indexes,
stored procedures, functions, views, and triggers.

## Learning Objectives

At the end of this project, I should be able to explain:

- How to create tables with constraints
- How to optimize queries by adding indexes
- What stored procedures and functions are in MySQL
- How to implement stored procedures and functions
- What views are in MySQL
- How to implement views
- What triggers are in MySQL
- How to implement triggers

## Requirements

- All files are executed on Ubuntu 20.04 LTS using MySQL 8.0
- All SQL files must end with a new line
- All SQL queries must have a comment before them
- All SQL files must start with a comment describing the task
- All SQL keywords must be written in uppercase

## Files

| File | Description |
| --- | --- |
| `0-uniq_users.sql` | Creates a `users` table with a unique email constraint |

## Usage

Run a SQL script with:

```bash
cat 0-uniq_users.sql | mysql -uroot -p database_name
```
