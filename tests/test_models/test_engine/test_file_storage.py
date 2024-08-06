#!/usr/bin/python3

"""
Test suite for the class FileStorage found in file_storage module
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """A class containing test cases for FileStorage class"""
    def test_1_all(self):
        """Test the all() method of FileStorage class"""
        storage_object = FileStorage()
        obj = BaseModel()
        # first set __objects attribute
        storage_object.new(obj)
        # check the if values in the dict is same as the object
        dictionary = storage_object.all()
        for key, value in dictionary.items():
            self.assertEqual(value, obj)

    def test_2_new(self):
        """Test the new() method of FileStorage class"""
        storage_object = FileStorage()
        obj = BaseModel()
        storage_object.new(obj)
        dictionary = storage_object.all()
        key = f'BaseModel.{obj.id}'
        self.assertEqual(dictionary.get(key), obj)

    def test_3_save(self):
        """Test the save() method of FileStorage class"""
        storage_object = FileStorage()
        file_path = "file.json"
        obj = BaseModel()
        key = f'BaseModel.{obj.id}'
        storage_object.new(obj)
        storage_object.save()

        with open(file_path, 'r') as file:
            content = file.read()
        self.assertIn(key, content)

    def test_4_reload(self):
        """Test the relaod() method of FileStorage class"""
        # since this test will be run 4th (by its name),
        # we expect test_3 to have created the file.json
        storage_object = FileStorage()
        storage_object.reload()
        dictionary = storage_object.all()
        # check if dictionary is not empty
        self.assertNotEqual(dictionary, None)
        print()
        print(dictionary)


if __name__ == '__main__':
    unittest.main()
