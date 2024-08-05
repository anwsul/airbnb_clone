#!/usr/bin/python3

"""
Contains a class BaseModel from which other classes inherit
"""
import copy
import uuid
from datetime import datetime

class BaseModel():
    """A base class from which other classes inherit"""
    def __init__(self):
        """Constructor for the BaseModel class"""
        # when an instance is created, it will have unique id
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of a BaseModel instance"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update the time when a BaseModel instance's attribute is modified"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of a BaseModel instance"""
        dictionary = copy.deepcopy(self.__dict__)
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary['created_at'] = datetime.isoformat(self.created_at)
        dictionary['updated_at'] = datetime.isoformat(self.updated_at)
        return dictionary
