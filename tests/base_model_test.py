#!/usr/bin/python3
"""Base Model Test #3"""
import unittest
from models.base import BaseModel
from unittest.mock import patch
from io import StringIO
import os


class TestBase(unittest.TestCase):
    """
    TEST: BASE CLASS TESTS
    """
    def test_save(self):
        """
        TEST:
        BaseMethod - save creates a save file
        """
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_created_at(self):
        new_model = BaseModel()
        self.assertIsInstance(new_model.create_at, "%Y-%m-%dT%H:%M:%S.%f")
        new_model2 = BaseModel()
        new_model = new_model2
        self.assertIsInstance(new_model.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

    def test_dict(self):
        """
        TEST:
        dict creates a str for updated and created
        and new instance class matches class name
        ADDING MORE STUFF BELOW LMAO (maybe itll work lol)
        (AHHHH)
        (oh lol)
        """
        new_model = BaseModel()
        new_dict = new_model.to_dict()
        self.assertIsInstance(new_dict, dict)
        self.assertIsInstance(new_dict["created_at"], str)
        self.assertIsInstance(new_dict["updated_at"], str)

    def test_str(self):
        """
        TEST:
        ___str___ method creates string instance
        """
        new_model = BaseModel()
        butt = new_model.__class__.__name__
        crack = new_model.id
        poop = new_model.to_dict()
        self.assertEqual(str(new_model),
            (f"[{butt}]({crack}) {poop}"))

    # unittest : init args / kwargs

"""DO NOT REMOVE"""
if __name__ == '__main__':
    unittest.main()
