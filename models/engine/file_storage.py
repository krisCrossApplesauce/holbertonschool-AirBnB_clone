#!/usr/bin/python3
""" yup """
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """ read/write and serialization for json storage """
    def __init__(self):
        self.__objects = dict()
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """return dict of __objects"""
        return self.__objects
    
    def new(self, obj):
        """add a new obj to __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialize obj to json file in __file_path"""
        ser_obj = {}
        for key, obj in self.__objects.items():
            ser_obj[key] = obj.to_dict()
    
        with open(self.__file_path, 'w') as file:
            json.dump(ser_obj, file)
    
    def reload(self):
        """deseriealize json file into __objects if it exists"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fp:
                for k, obj_data in json.load(fp).items():
                    if k not in FileStorage.__objects:
                        cls = FileStorage.__models[obj_data["__class__"]]
                        FileStorage.__objects[k] = cls(**obj_data)
        else:
            with open(FileStorage.__file_path, 'w') as fp:
                fp.write("{}")
