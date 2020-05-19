#!/usr/bin/python3
"""creating a class"""


class Square:
    """Defines a square with one property: a writable size.

    Attributes:
        size: (:obj: `int`, optional): private instance.
        area: (:obj: `int`): public instance method, returns square area.

    Raises:
        TypeError: An exception if parameter size is not an integer.
        ValueError: An exception if parameter size is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2
            or type(value) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for w in range(self.size):
                for i in range(self.position[0]):
                    print(end=" ")
                for h in range(self.size):
                    print("#", end="")
                print()
