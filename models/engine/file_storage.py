#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import os


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): file path to save the object.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        json_obj = {}
        for key in self.__objects.keys():
            json_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as json_file:
            json.dump(json_obj, json_file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                json_obj = json.load(json_file)
                for key in json_obj.keys():

                    # By providing the dict value stored in json_obj[key] as
                    # kwargs, genrate an object with the same attributes
                    self.__objects[key] = eval(
                        json_obj[key]['__class__'])(**json_obj[key])
                    
    def delete(self, obj=None):
        """Delete an object from the __objects"""
        if obj is not None:
            for key, val in list(FileStorage.__objects.items()):
                if obj == val:
                    del FileStorage.__objects[key]
                    print("Deleted: {}".format(key))
                    self.save()
                    
    def close(self):
        """calls the reload instance"""
        self.reload()

