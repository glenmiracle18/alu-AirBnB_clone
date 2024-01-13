#!/usr/bin/env python
"""A module that that serializes instances to a JSON file and deserializes
JSON file to instances"""

import json


class FileStorage:
    """"file storage main instance"""

    # private class attributes
    # __file_path is the path to the JSON file to store all objects.
    __file_path = 'file.json'

    # __objects is a dictionary that stores all objects by <class name>.id
    # ex: to store a BaseModel object with id=12121212, the key will be
    # BaseModel.12121212 and the value will be the object.
    # the object (value of key) is stored like this:
    # <models.base_model.BaseModel object at 0x7f3329dac310>
    # obects = {BaseModel.12121212: }
    __objects = {}

    def all(self, cls=None):
        """Returns a list of all objects if cls is None.
        """
        return FileStorage.__objects

    # sets in __objects the obj with key <obj class name>.id
    def new(self, obj):
        """Add obj with key <obj class name>.id to dictionary.

        Args:

        obj: the object with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        # json_data = json.dump(obj)
        self.__objects[key] = obj

    # serializes __objects to the JSON file (path: __file_path)
    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)."""
        json_obj = {}
        for key in self.__objects.keys():
            json_obj[key] = self.__objects[key].to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(json_obj, json_file)

    def reload(self):
        """
        reloads all the objs saved in file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.city import City
        from models.state import State
        from models.review import Review
        myclasses = {"BaseModel": BaseModel, "User": User, "Place": Place,
                     "Amenity": Amenity, "City": City, "State": State,
                     "Review": Review}
        try:
            with open(FileStorage.__file_path, "r") as f:
                my_dict = json.load(f)
                for k, v in my_dict.items():
                    FileStorage.__objects[k] = myclasses[v["__class__"]](**v)
        except Exception:
            pass

    def delete(self, obj=None):
        """Delete an object from the __objects"""
        if obj is not None:
            for key, val in list(FileStorage.__objects.items()):
                if obj == val:
                    del FileStorage.__objects[key]
                    print("Deleted: {}".format(key))
                    self.save()

    def close(self):
        """closing instance"""
        self.reload()
