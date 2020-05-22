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
        self.size = size
        self.position = position

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
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
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

    def __str__(self):
        allstr = ""
        if self.position[1] == 1:
            allstr += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                allstr += " "
            for h in range(self.size):
                allstr += "#"
            if w != self.size - 1:
                allstr += "\n"
        return allstr
