#!/usr/bin/python3
""" Unittest for File Storage """
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
import unittest
import os
import json


class FileStorageTest(unittest.TestCase):
    """Unittests for FileStorage"""

    def test_attributes(self):
        """
        test_attributes
        """
        new_fs = FileStorage()
        self.assertFalse(hasattr(new_fs.__file_path, '__file_path'))
        self.assertFalse(hasattr(new_fs.__objects, '__objects'))

    def test_all_empty(self):
        """Test all empty"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        new_fs = FileStorage()
        self.assertEqual(new_fs.all(), {})

    def test_new_object(self):
        """Test new object"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        a_fs = FileStorage()
        new_user = User()
        a_fs.new(new_user)
        expected = {f"User.{new_user.id}": new_user}
        self.assertEqual(a_fs.all(), expected)

    def test_save_object(self):
        """Test save objects"""
        new_fs = FileStorage()
        new_user = User()
        new_fs.new(new_user)
        new_fs.save()
        key = f"User.{new_user.id}"
        with open("file.json", "r") as file:
            file_content = json.load(file)
            self.assertTrue(file_content.get(key))

    def test_reload_file_not_exist(self):
        """Test reload file not exists"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            new_fs = FileStorage()
            new_fs.reload()
        except Exception:
            self.fail()

    def test_reload_file_exists(self):
        """Test reload file exists"""
        new_fs = FileStorage()
        new_fs.reload()
        content = new_fs.all()
        self.assertNotEqual(content, {})

    def test_all_non_empty(self):
        """Test all none empty"""
        new_fs = FileStorage()
        new_user = User()
        new_base_model = BaseModel()
        new_fs.new(new_user)
        new_fs.new(new_base_model)
        self.assertNotEqual(new_fs.all(), {})


if __name__ == "__main__":
    unittest.main()
