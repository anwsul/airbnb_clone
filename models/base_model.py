#!/usr/bin/python3

"""
Contains a class BaseModel from which other classes inherit
"""
import copy
import uuid
import models
from datetime import datetime


class BaseModel():
    """A base class from which other classes inherit"""
    def __init__(self, *args, **kwargs):
        """Constructor for the BaseModel class"""
        # if a dictionary is passed, create the instance from it
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)

        else:
            # when an instance is created, it will have unique id
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of a BaseModel instance"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update the time when a BaseModel instance's attribute is modified"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of a BaseModel instance"""
        dictionary = copy.deepcopy(self.__dict__)
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary['created_at'] = datetime.isoformat(self.created_at)
        dictionary['updated_at'] = datetime.isoformat(self.updated_at)
        return dictionary
