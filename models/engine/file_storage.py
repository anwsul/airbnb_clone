#!/usr/bin/python3

"""
Contains the FileStorage class used to serializes instances of BaseModel
to a JSON file and deserializes JSON file to BaseModel instances
"""


import json
from os import path


class FileStorage():
    """A class for serializing & deserializing instances"""
    # where the JSON representaion of the object is stored
    __file_path = "file.json"
    # store objects by <class name>.id as their key
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects, the obj with key <obj class name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        # serializing each values(objects) in __objects to dictionary
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(new_dict, fp)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        # to hold the deserialized dict
        new_dict = {}
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fp:
                new_dict = json.load(fp)
            for key, value in new_dict.items():
                class_name = value['__class__']
                # creating the instance from the classname and a dictionary
                object = eval(class_name)(** value)
                self.new(object)
