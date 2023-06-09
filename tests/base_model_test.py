#!/usr/bin/python3
"""Base Model Test #3"""
import unittest
from models.base import BaseModel
from unittest.mock import patch
from io import StringIO

class TestBase(unittest.TestCase):
    """
    TEST: BASE CLASS TESTS
    """
    def test_save(self):
        """TEST: save creates a saved file"""
        b1 = BaseModel()
        saved_data = BaseModel.save([b1])
        self.assertEqual(len(saved_data), b1.updated_at) 
            # compare saved data to updated_at of new instance

    def test_dict(self):
        """TEST: dict creates two strings for each updated and created
        also, the created class for the instance == class name
        """
        b2 = BaseModel()
        b2 = self.__dict__copy()
        self.assertIsInstance(self.create_at, _______)
        self.assertIsInstance(self.updated_at, _______)
        for element in self.__dict__
            self.assertEqual(b1['class'], self.__dict__.__class__) 
                # compare created dict keys to class names of the instance

"""DO NOT REMOVE"""
if __name__ == '__main__':
    unittest.main()
