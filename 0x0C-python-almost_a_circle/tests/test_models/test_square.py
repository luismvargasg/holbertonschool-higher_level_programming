#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """defining the Unittest for class Square"""

    def setUp(self):
        """method called to default initialize a Square"""
        self.obj = Square(1)

    def tearDown(self):
        """cleaning the attribute nb_objects counter to 0"""
        Base._Base__nb_objects = 0

    def test_pep8_conformance(self):
        """Test square.py file with PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/square.py"])
        self.assertEqual(result.total_errors, 0, "Found code style " +
                         "errors (and warnings).")

    def test_is_instance(self):
        """testing if a new Square is an instance."""
        self.assertIsInstance(self.obj, Square, "created obj is not an " +
                              "instance of Square class.")

    def test_inherits_from_Rectangle(self):
        """testing if a new Square inherits from Rentagle class"""
        self.assertIsInstance(self.obj, Rectangle, "created obj does not " +
                              "inherit from the Base class.")

    def test_default_init(self):
        """testing if the default initialization has the right values"""
        self.assertEqual(self.obj.size, 1)
        self.assertEqual(self.obj.x, 0)
        self.assertEqual(self.obj.y, 0)
        self.assertEqual(self.obj.id, 1)

    def test_square_partial_init(self):
        """testing if the initialization with some of the given args
        has the right values assigned to each attribute"""
        r1 = Square(5, 4, 0)
        self.assertEqual(r1.size, 5)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 2)

    def test_square_full_init(self):
        """testing if the initialization with all the given args
        has the right values assigned to each attribute"""
        r2 = Square(10, 2, 1, 3)
        self.assertEqual(r2.size, 10)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.id, 3)

    def test_raise_TypeError_morearg(self):
        """testing if the TypeError: "__init__() takes from 2 to 5 positional
        arguments but 7 were given" is raised"""
        self.assertRaises(TypeError, Square, 1, 2, 3, 4, 5, 6)

    def test_raise_TypeError_noarg(self):
        """testing if the TypeError: "__init__() missing 2 required positional
        arguments: 'width' and 'height'" is raised"""
        self.assertRaises(TypeError, Square)
