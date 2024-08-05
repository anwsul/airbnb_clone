#!/usr/bin/python3

"""
A test suite for BaseModel class, found inside base_model module
"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """A class to test the methods available for BaseModel class"""
    def test_init(self):
        """Test the constructor of BaseModel class"""
        instance = BaseModel()
        # check if id attribute exists
        self.assertTrue(instance.id)
        # check if created_at attribute exists
        self.assertTrue(instance.created_at)
        # check if updated_at attribute exists
        self.assertTrue(instance.updated_at)
        # check if the id attribute is of type string
        self.assertEqual(type(instance.id), str)

    def test_str(self):
        """Test the str() method of BaseModel"""
        instance = BaseModel()
        instance.id = 5

        # expected string representation
        expected_str = f'[BaseModel] (5) {instance.__dict__}'

        self.assertEqual(expected_str, str(instance))

    def test_save(self):
        """Test the save method"""
        instance = BaseModel()
        initial_time = instance.updated_at
        instance.save()
        final_time = instance.updated_at
        # check if the updated_at attribute is updated
        self.assertNotEqual(initial_time, final_time)

    def test_to_dict(self):
        """Test test_to_dict method"""
        instance = BaseModel()
        # check the type to_dict() returns
        self.assertEqual(type(instance.to_dict()), dict)
        # check if the value for the key __class__
        dictionary = instance.to_dict()
        self.assertEqual(dictionary.get('__class__'), 'BaseModel')
        # check if the type of created_at is a string
        self.assertEqual(type(dictionary.get('created_at')), str)
        # check if the type of updated_at is a string
        self.assertEqual(type(dictionary.get('updated_at')), str)


if __name__ == '__main__':
    unittest.main()
