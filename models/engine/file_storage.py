#!/usr/bin/python3
"""
location for storing data
after EOF and exiting
"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """read/write and serialization for json storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dict of __objects"""
        return self.__objects

    def new(self, obj):
        """add a new obj to __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def update(self, obj, key, value):
        """ update """
        setattr(obj, key, value)
        self.save()

    def save(self):
        """serialize obj to json file in __file_path"""
        ser_obj = {}
        for key, obj in self.__objects.items():
            ser_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(ser_obj, file)

    def reload(self): # double check this!
        """deseriealize json file into __objects if it exists"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                for key, obj_data in json.load(file).items():
                    if key not in self.__objects:
                        obj = eval(obj_data["__class__"])
                        self.__objects[key] = obj(**obj_data)
        else:
            with open(self.__file_path, 'w') as file:
                file.write("{}")

    def remove(self, key):
        """REMOVE THE THING and then save the change to the json file"""
        del self.__objects[key]
        self.save()
