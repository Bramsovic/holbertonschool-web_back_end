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
| `1-country_users.sql` | Creates a `users` table with a country enumeration |
| `2-fans.sql` | Ranks band origins by total number of fans |
| `3-glam_rock.sql` | Lists Glam rock bands ranked by lifespan |
| `4-store.sql` | Creates a trigger to decrease item quantity after an order |
| `5-valid_email.sql` | Creates a trigger to reset email validation when email changes |
| `6-bonus.sql` | Creates a stored procedure to add bonus corrections |
| `7-average_score.sql` | Creates a stored procedure to compute a user's average score |
| `8-index_my_names.sql` | Creates an index on the first letter of names |
| `9-index_name_score.sql` | Creates an index on the first letter of names and score |
| `10-div.sql` | Creates a function that divides two numbers safely |
| `11-need_meeting.sql` | Creates a view of students who need a meeting |

## Usage

Run a SQL script with:

```bash
cat 0-uniq_users.sql | mysql -uroot -p database_name
```
