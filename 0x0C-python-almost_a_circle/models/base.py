#!/usr/bin/python3
"""Defining the Base class"""
import json
import turtle


class Base:
    """This class will be the base of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor for Base.

        Args:
            id: is an integer, if id is not None, id with this argument
            value is assigned, otherwise __nb_objects is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation
        of list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(cls.to_dictionary(obj))
        with open(filename, mode="w", encoding="utf-8") as myFile:
            myFile.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string
        representation json_string.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all attributes
        already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        objs = []
        try:
            with open(filename, mode="r", encoding="utf-8") as myFile:
                objs = cls.from_json_string(myFile.read())
            for key, value in enumerate(objs):
                objs[key] = cls.create(**objs[key])
        except:
            pass
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """static method that opens a window and draws all
        the Rectangles and Squares."""
        turtle.title("OOP in Python - drawing in GUI")
        turtle.setup(width=1000, height=600)
        turtle.bgcolor("#29293d")
        turtle.pen(pencolor="#8080ff", pensize="4")
        turtle.penup()
        turtle.goto(x=0, y=300)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(600)

        titles = turtle.Turtle()
        titles.hideturtle()
        titles.penup()
        titles.goto(x=-330, y=260)
        titles.color("#ffff66")
        titles.write("Rectangles", font=("Arial", 28, 'bold'))
        titles.goto(x=195, y=260)
        titles.color("#ffff66")
        titles.write("Squares", font=("Ar#212145ial", 28, 'bold'))

        coord_x = -270
        coord_y = 100
        aux_turtle = turtle.Turtle()
        for obj in list_rectangles:
            w = obj.width
            h = obj.height
            x = obj.x
            y = obj.y

            titles.goto(coord_x - 180, coord_y + 50)
            titles.color("white")
            titles.write(obj, font=("Arial", 11, 'bold'))
            turtle.penup()
            aux_turtle.penup()
            turtle.goto(coord_x, coord_y)
            aux_turtle.goto(coord_x, coord_y)
            turtle.pen(pencolor="#ff6666", pensize="2.5", fillcolor="#212145")
            aux_turtle.pen(pencolor="gray", pensize="1.5")
            aux_turtle.pendown()
            aux_turtle.forward(140)
            aux_turtle.left(180)
            aux_turtle.forward(140)
            aux_turtle.right(90)
            aux_turtle.forward(140)
            turtle.goto(coord_x + x, coord_y + y)
            turtle.pendown()
            for i in range(2):
                turtle.left(90)
                turtle.forward(w)
                turtle.left(90)
                turtle.forward(h)
            coord_y -= 190
            aux_turtle.right(90)

        coord_x = 230
        coord_y = 100
        for obj in list_squares:
            w = obj.width
            h = obj.height
            x = obj.x
            y = obj.y

            titles.goto(coord_x - 160, coord_y + 50)
            titles.color("white")
            titles.write(obj, font=("Arial", 11, 'bold'))
            turtle.penup()
            aux_turtle.penup()
            turtle.goto(coord_x, coord_y)
            aux_turtle.goto(coord_x, coord_y)
            turtle.pen(pencolor="#ff6666", pensize="2.5", fillcolor="#212145")
            aux_turtle.pen(pencolor="gray", pensize="1.5")
            aux_turtle.pendown()
            aux_turtle.forward(140)
            aux_turtle.left(180)
            aux_turtle.forward(140)
            aux_turtle.right(90)
            aux_turtle.forward(140)
            turtle.goto(coord_x + x, coord_y + y)
            turtle.pendown()
            for i in range(4):
                turtle.left(90)
                turtle.forward(w)
            coord_y -= 190
            aux_turtle.right(90)

        turtle.done()
