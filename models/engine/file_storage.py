#!/usr/bin/python3
""" yup """
import json
import os

class FileStorage:
    """ yup """
    def __init__(self):
        #if new instance add
        # a call to the method: new(self) on 'storage'
        self.__file_path = ""
        self.__objects = []

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ser_obj = {}
        for key, obj in self.__objects.items():
            ser_obj[key] = obj.to_dict()
    
        with open(self.__file_path, 'w') as file:
            json.dump(ser_obj, file)

        #create a string representation of the saved filepath
        #saved to __file_path
    
    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                objects = json.load(file)

            for key, des_obj in objects.items():
                class_name, obj_id = key.split('.')
                model = __import__('models.' + class_name, fromlist=[class_name])
                cls = getattr(model, class_name)
                obj = cls(**des_obj)
                self.__objects[key] = obj
