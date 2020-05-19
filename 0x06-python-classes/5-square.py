#!/usr/bin/python3
class Square:
    """Defines a square with one property: a writable size.

    Attributes:
        size: (:obj: `int`, optional): private instance.
        area: (:obj: `int`): public instance method, returns square area.

    Raises:
        TypeError: An exception if parameter size is not an integer.
        ValueError: An exception if parameter size is less than 0.
    """

    def __init__(self, size=0):
        # if type(size) is not int:
        #    raise TypeError("size must be an integer")
        # elif size < 0:
        #    raise ValueError("size must be >= 0")
        # else:
        self.__size = size

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

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for w in range(self.size):
                for h in range(self.size):
                    print("#", end="")
                print()
