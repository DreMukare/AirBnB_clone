#!/usr/bin/python3
"""
    module: FileStorage
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
        class FileStorage
        private class attributes:
            __file_path(str): path to the JSON file
            __objects(dict): will store all objects by <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            returns __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def classes(self):
        """ Returns a dict of all valid classes """
        classes = {"BaseModel": BaseModel,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review,
                   "User": User}
        return classes

    def save(self):
        """
            serializes __objects to the JSON file
        """
        obj_dicts = {}
        for k, v in self.__objects.items():
            obj_dicts[k] = v.to_dict()
        with open(self.__file_path, 'w+') as f:
            json.dump(obj_dicts, f)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dicts = json.load(json_file)

            my_objs = {}
            for k, v in obj_dicts.items():
                class_name = v['__class__']
                my_objs[k] = eval(class_name)(**v)
            self.__objects.update(my_objs)
