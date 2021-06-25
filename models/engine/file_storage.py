#!/usr/bin/python3
"""
    module: FileStorage
"""
import json
import os

class FileStorage:
    """
        class FileStorage
        private class attributes:
            __file_path(str): path to the JSON file
            __objects(dict): will store all objects by <class name>.id
    """
    __file_path = 'BaseModel.json'
    __objects = {}

    def all(self):
        """
            returns __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        if obj == {} or obj is None:
            return
        key = obj["__class__"] + "." + obj["id"]
        FileStorage.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
            with open(FileStorage.__file_path, 'w') as f:
                json.dump(FileStorage.__objects, f)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        else:
            pass