#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """defining the Unittest for class Base"""

    def setUp(self):
        """method called to initialize an obj of Base class with id 1"""
        self.obj = Base()

    def tearDown(self):
        """cleaning the attribute nb_objects counter to 0"""
        Base._Base__nb_objects = 0

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/base.py"])
        self.assertEqual(result.total_errors, 0, "Found code style " +
                         "errors (and warnings).")

    def test_is_instance(self):
        """testing if a new object is an instances of the Base class"""
        self.assertIsInstance(self.obj, Base, "created obj is not an " +
                              "instance of Base class.")

    def test_hasattr_nb_objects(self):
        """testing if the created object has the __nb_objects attribute"""
        self.assertTrue(hasattr(self.obj, "_Base__nb_objects"), "created " +
                        "obj doesn't have the attribute __nb_objects.")

    def test_hasattr_id(self):
        """testing if the created object has the id attribute"""
        self.assertTrue(hasattr(self.obj, "id"), "created obj doesn't " +
                        "have the attribute id.")

    def test_base_id_auto(self):
        """testing the id constructor with auto id assignation"""
        self.assertEqual(self.obj.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_base_id_manual(self):
        """testing the id constructor with manual id assignation"""
        b4 = Base(8)
        self.assertEqual(b4.id, 8)
        b5 = Base(9)
        self.assertEqual(b5.id, 9)

    def test_base_id_both(self):
        """testing the id constructor with auto and manual id assignation"""
        self.assertEqual(self.obj.id, 1)
        b6 = Base()
        self.assertEqual(b6.id, 2)
        b7 = Base()
        self.assertEqual(b7.id, 3)
        b8 = Base(99)
        self.assertEqual(b8.id, 99)
        b9 = Base(-99)
        self.assertEqual(b9.id, -99)

    def test_raise_TypeError(self):
        """testing if the TypeError: "__init__() takes from 1 to 2 positional
        arguments but 3 were given" is raised"""
        self.assertRaises(TypeError, Base, 1, 2)
