#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """defining the Unittest for class Recatangle"""

    def setUp(self):
        """method called to default initialize a rectangle"""
        self.obj = Rectangle(1, 1)

    def tearDown(self):
        """cleaning the attribute nb_objects counter to 0"""
        Base._Base__nb_objects = 0

    def test_pep8_conformance(self):
        """Test rectangle.py file with PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/rectangle.py"])
        self.assertEqual(result.total_errors, 0, "Found code style " +
                         "errors (and warnings).")

    def test_is_instance(self):
        """testing if a new rectangle is an instance."""
        self.assertIsInstance(self.obj, Rectangle, "created obj is not an " +
                              "instance of Rectangle class.")

    def test_inherits_from_base(self):
        """testing if a new rectangle inherits from Base class"""
        self.assertIsInstance(self.obj, Base, "created obj does not " +
                              "inherit from the Base class.")

    def test_hasattrs(self):
        """testing if the created object has all the attributes"""
        self.assertTrue(hasattr(self.obj, "id"), "created obj doesn't " +
                        "have the attribute id.")
        self.assertTrue(hasattr(self.obj, "_Rectangle__width"), "created " +
                        "obj doesn't have the attribute width.")
        self.assertTrue(hasattr(self.obj, "_Rectangle__height"), "created " +
                        "obj have the attribute height.")
        self.assertTrue(hasattr(self.obj, "_Rectangle__x"), "created obj " +
                        "doesn't have the attribute x.")
        self.assertTrue(hasattr(self.obj, "_Rectangle__y"), "created " +
                        "obj doesn't have the attribute y.")

    def test_raise_TypeError_onearg(self):
        """testing if the TypeError: "__init__() missing 1 required positional
        argument: 'height'" is raised"""
        self.assertRaises(TypeError, Rectangle, 1)

    def test_raise_TypeError_noarg(self):
        """testing if the TypeError: "__init__() missing 2 required positional
        arguments: 'width' and 'height'" is raised"""
        self.assertRaises(TypeError, Rectangle)

    def test_raise_TypeError_morearg(self):
        """testing if the TypeError: "__init__() takes from 3 to 6 positional
        arguments but 7 were given" is raised"""
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6)

    def test_default_init(self):
        """testing if the default initialization has the right values"""
        self.assertEqual(self.obj.width, 1)
        self.assertEqual(self.obj.height, 1)
        self.assertEqual(self.obj.x, 0)
        self.assertEqual(self.obj.y, 0)
        self.assertEqual(self.obj.id, 1)

    def test_rectangle_partial_init(self):
        """testing if the initialization with some of the given args
        has the right values assigned to each attribute"""
        r1 = Rectangle(5, 4, 0, 0)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 2)

    def test_rectangle_full_init(self):
        """testing if the initialization with all the given args
        has the right values assigned to each attribute"""
        r2 = Rectangle(10, 2, 1, 3, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, 12)

    def test_raise_TypeError_morearg(self):
        """testing if the TypeError: "__init__() takes from 3 to 6 positional
        arguments but 7 were given" is raised"""
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6)
