#!/usr/bin/python3
"""
    module: FileStorage
"""
import json


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
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        if obj == {} or obj is None:
            return
        # key = obj.__class__.__name__ + "." + obj["id"]
        key = obj.__class__.__name__ + '.' + str(obj)
        FileStorage.__objects[key] = obj

    def classes(self):
        """ Returns a dict of all valid classes """
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        from models.user import User

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
        with open(FileStorage.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp_dict = json.loads(FileStorage.__objects, f)
                for v in temp_dict.values():
                    cls = v['__class__']
                    self.new(eval(cls)(**v))
        except Exception:
            pass
