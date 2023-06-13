#!/usr/bin/python3
"""TEST: File storage"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.model1 = BaseModel()
        self.model2 = BaseModel()
        self.storage.new(self.model1)
        self.storage.new(self.model2)

    def test_all(self):
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 2)

    def test_new(self):
        key = f"{self.model1.__class__.__name__}.{self.model1.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), 2)

        key = f"{self.model1.__class__.__name__}.{self.model1.id}"
        self.assertIn(key, objects)

    def test_reload_file_not_found(self):
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)

    def test_reload_empty_file(self):
        with open(self.file_path, "w") as file:
            file.write("")

        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)

if __name__ == "__main__":
    unittest.main()