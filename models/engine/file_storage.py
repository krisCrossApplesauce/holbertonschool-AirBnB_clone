#!/usr/bin/python3
""" yup """
import json
import os
# from models.base_model import BaseModel # not accessed error

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
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                objects = json.load(file)

            for key, des_obj in objects.items():
                class_name = key.split('.')[0] # shorthand for referencing id?
                model = __import__('models.' + class_name, fromlist=[class_name])
                cls = getattr(model, class_name)
                obj = cls(**des_obj)
                self.__objects[key] = obj
