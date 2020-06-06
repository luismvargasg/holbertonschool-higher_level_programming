# 0x0C. Python - Almost a circle

> This directory contains all the tasks of the project "0x0C. Python - Almost a circle" at [Holberton School](https://www.holbertonschool.com "Holberton School.") for educational purpose.

## General Objectives

* What is Unit testing and how to implement it in a large project.
* How to serialize and deserialize a Class.
* How to write and read a JSON file.
* What is *args and how to use it.
* What is **kwargs and how to use it.
* How to handle named arguments in a function.

## Basic info

In this project, you will review everything about Python:

* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file

You will also learn about:

* args and kwargs
* Serialization/Deserialization
* JSON

For more information please visit: [args / kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)

## Directory Files

| **File** | **Description** |
|----------|-----------------|
| [0. If it's not tested it doesn't work](./tests) | All your files, classes and methods must be unit tested and be PEP 8 validated. |
| [1. Base class](./models/base.py) | Write the first class Base |
| [1. Base class](./models/__init__.py) | Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python module |
| [2. First Rectangle](./models/rectangle.py) | Write the class Rectangle that inherits from Base. |
| [3. Validate attributes](./models/rectangle.py) | Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded) |
| [4. Area first](./models/rectangle.py) | Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance. |
| [5. Display #0](./models/rectangle.py) | Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you dont need to handle x and y here. |
| [6. __str__](./models/rectangle.py) | Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height> |
| [7. Display #1](./models/rectangle.py) | Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y |
| [8. Update #0](./models/rectangle.py) | Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute. |
| [9. Update #1](./models/rectangle.py] | Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes |
| [10. And now, the Square!](./models/square.py) | Write the class Square that inherits from Rectangle. |
| [11. Square size](./models/square.py) | Update the class Square by adding the public getter and setter size. |
| [12. Square update](./models/square.py) | Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes. |
| [13. Rectangle instance to dictionary representation](./models/rectangle.py) | Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle. |
| [14. Square instance to dictionary representation](./models/square.py) | Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square. |
| [15. Dictionary to JSON string](./models/base.py) | Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries. |
| [16. JSON string to file](./models/base.py) | Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file. |
| [17. JSON string to dictionary](./models/base.py) | Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string. |
| [18. Dictionary to Instance](./models/base.py) | Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set. |
| [19. File to instances](./models/base.py) | Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances. |
| [20. JSON ok, but CSV?](./models/) | Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV |
| [21. Let's draw it](./models/base.py) | Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares. |

## Author

* [GitHub - Luis Miguel Vargas](https://github.com/luismvargasg)

* [LinkedIn - Luis Miguel Vargas](https://www.linkedin.com/in/luismvargasg/)
