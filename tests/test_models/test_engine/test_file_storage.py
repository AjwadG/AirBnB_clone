#!/usr/bin/python3
""" Unittest for File Storage """
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
import unittest
import os
import json


class FileStorageTest(unittest.TestCase):
    """Unittests for FileStorage"""

    def test_wrong_args(self):
        '''all the methods with wrong args'''
        try:
            os.remove("file.json")
        except IOError:
            pass
        with self.assertRaises(TypeError):
            FileStorage(None)
        with self.assertRaises(TypeError):
            storage.save(None)
        with self.assertRaises(TypeError):
            storage.all("what")
        with self.assertRaises(AttributeError):
            storage.new("is")
        with self.assertRaises(TypeError):
            storage.save("you'r")
        with self.assertRaises(TypeError):
            storage.reload("Name")

    def test_attributes(self):
        """
        test_attributes
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertFalse(hasattr(storage, '__file_path'))
        self.assertFalse(hasattr(storage, '__objects'))
        self.assertEqual(type(storage), FileStorage)

    def test_all_empty(self):
        """Test all empty"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        new_fs = FileStorage()
        FileStorage._FileStorage__objects = {}
        new_fs.reload()
        self.assertEqual(new_fs.all(), {})
        self.assertEqual(dict, type(new_fs.all()))

    def test_new_object(self):
        """Test new object"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        a_fs = FileStorage()
        FileStorage._FileStorage__objects = {}
        new_user = User()
        new_BM = BaseModel()
        a_fs.new(new_user)
        a_fs.new(new_BM)
        expected = {f"User.{new_user.id}": new_user,
                    f"BaseModel.{new_BM.id}": new_BM}
        self.assertEqual(a_fs.all(), expected)

    def test_save_object(self):
        """Test save objects"""
        new_fs = FileStorage()
        new_user = User()
        new_fs.new(new_user)
        new_BM = BaseModel()
        new_fs.save()
        U_key = f"User.{new_user.id}"
        BM_key = f"BaseModel.{new_BM.id}"
        with open("file.json", "r") as file:
            file_content = json.load(file)
            self.assertTrue(file_content.get(U_key))
            self.assertTrue(file_content.get(BM_key))

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
        storage.reload()
        content = storage.all()
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
