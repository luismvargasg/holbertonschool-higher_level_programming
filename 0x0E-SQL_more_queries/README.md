# SQL - More queries

> This directory contains all the tasks of the project "0x0E. SQL - More queries" at [Holberton School](https://www.holbertonschool.com "Holberton School.") for educational purpose.

## Table of Contents

- [SQL - More queries](#sql---more-queries)
  - [Table of Contents](#table-of-contents)
  - [General Objectives](#general-objectives)
  - [Basic info](#basic-info)
  - [Directory Files](#directory-files)
  - [Built With](#built-with)
  - [Author](#author)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## General Objectives

* How to create a new MySQL user.
* How to manage privileges for a user to a database or table.
* What’s a PRIMARY KEY.
* What’s a FOREIGN KEY.
* How to use NOT NULL and UNIQUE constraints.
* How to retrieve datas from multiple tables in one request.
* What are subqueries.
* What are JOIN and UNION.

## Basic info

MySQL is an open-source database management software that helps users store, organize, and later retrieve data. It has a variety of options to grant specific users nuanced permissions within the tables and databases.

For more information please visit: [SQL Command Cheatsheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)

## Directory Files

| **File** | **Description** |
|----------|-----------------|
| [0. My privileges!](./0-privileges.sql) | Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost). |
| [1. Root user](./1-create_user.sql) | Write a script that creates the MySQL server user user_0d_1. |
| [2. Read user](./2-create_read_user.sql) | Write a script that creates the database hbtn_0d_2 and the user user_0d_2. |
| [3. Always a name](./3-force_name.sql) | Write a script that creates the table force_name on your MySQL server. |
| [4. ID can't be null ](./4-never_empty.sql) | Write a script that creates the table id_not_null on your MySQL server. |
| [5. Unique ID](./5-unique_id.sql) | Write a script that creates the table unique_id on your MySQL server. |
| [6. States table](./6-states.sql) | Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server. |
| [7. Cities table](./7-cities.sql) | Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server. |
| [8. Cities of California](./8-cities_of_california_subquery.sql) | Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa. |
| [9. Cities by States](./9-cities_by_state_join.sql) | Write a script that lists all cities contained in the database hbtn_0d_usa. |
| [10. Genre ID by show](./10-genre_id_by_show.sql) | Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked. |
| [11. Genre ID for all shows](./11-genre_id_all_shows.sql) | Write a script that lists all shows contained in the database hbtn_0d_tvshows. |
| [12. No genre](./12-no_genre.sql) | Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked. |
| [13. Number of shows by genre](./13-count_shows_by_genre.sql) | Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each. |
| [14. My genres](./14-my_genres.sql) | Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter. |
| [15. Only Comedy](./15-comedy_only.sql) | Write a script that lists all Comedy shows in the database hbtn_0d_tvshows. |
| [16. List shows and genres](./16-shows_by_genre.sql) | Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows. |

## Built With

* Ubuntu 14.04.3 LTS Running on a Virtual Machine "Vagrant"
* GNU Emacs 24.3.1
* MySQL 5.7

## Author

* [GitHub - Luis Miguel Vargas](https://github.com/luismvargasg)

* [LinkedIn - Luis Miguel Vargas](https://www.linkedin.com/in/luismvargasg/)

## License

Opensource project.

## Acknowledgments

* Project made at Holberton School - Colombia.
