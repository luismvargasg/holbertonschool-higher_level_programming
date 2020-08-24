# Python - Network #1

> This directory contains all the tasks of the project "0x11. Python - Network #1" at [Holberton School](https://www.holbertonschool.com "Holberton School.") for educational purpose.


[![Luis Miguel Vargas](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Fluismvargasg1)](https://twitter.com/luismvargasg1)

## Table of Contents

- [Python - Network #1](#python---network-1)
  - [Table of Contents](#table-of-contents)
  - [General Objectives](#general-objectives)
  - [Basic info](#basic-info)
  - [Directory Files](#directory-files)
  - [Built With](#built-with)
  - [Author](#author)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## General Objectives

* How to fetch internet resources with the Python package urllib.
* How to decode urllib body response.
* How to use the Python package requests #requestsiswaysimplerthanurllib.
* How to make HTTP GET request.
* How to make HTTP POST/PUT/etc. request.
* How to fetch JSON resources.
* How to manipulate data from an external service.

## Basic info

Please visit:
- [HOWTO Fetch Internet Resources Using The urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Requests: HTTP for Humans™](https://requests.readthedocs.io/en/master/)

## Directory Files

| **File** | **Description** |
|----------|-----------------|
| [0. What's my status? #0](./0-hbtn_status.py) | Script that fetches https://intranet.hbtn.io/status |
| [1. Response header value #0](./1-hbtn_header.py) | Script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response. |
| [2. POST an email #0](./2-post_email.py) | Script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) |
| [3. Error code #0](./3-error_code.py) | Script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8). |
| [4. What's my status? #1](./4-hbtn_status.py) | Script that fetches https://intranet.hbtn.io/status |
| [5. Response header value #1](./5-hbtn_header.py) | Script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header. |
| [6. POST an email #1](./6-post_email.py) | Script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response. |
| [7. Error code #1](./7-error_code.py) | Script that takes in a URL, sends a request to the URL and displays the body of the response. |
| [8. Search API](./8-json_api.py) | Script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter. |
| [9. My Github!](./10-my_github.py) | Script that takes your Github credentials (username and password) and uses the Github API to display your id. |

## Built With

* Ubuntu 14.04.3 LTS Running on a Virtual Machine "Vagrant"
* GNU Emacs 24.3.1

## Author

* [GitHub - Luis Miguel Vargas](https://github.com/luismvargasg)

* [LinkedIn - Luis Miguel Vargas](https://www.linkedin.com/in/luismvargasg/)

## License

Opensource project.

## Acknowledgments

* Project made at Holberton School - Colombia.
