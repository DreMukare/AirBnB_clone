#!/usr/bin/python3
"""
module: class BaseModel
contains methods for persistence of data
keeps track of it's number of instances
"""
from models import storage
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
        class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
            initializes all instances of BaseModel
            attributes:
                id(string): unique id for every instance of BaseModel
                created_at(datetime): time at which instance was created
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime\
                        .strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime\
                        .strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                self.id = str(uuid4())
                self.created_at = datetime\
                    .now().strftime('%Y-%m-%dT%H:%M:%S.%f')
                storage.new(self)

    def __str__(self):
        """
            prints a string representation of BaseClass instance
        """
        return '[{}] ({}) <{}>'\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        storage.save()
        self.updated_at = datetime\
            .now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        dict = self.__dict__
        dict['__class__'] = self.__class__.__name__
        return dict
