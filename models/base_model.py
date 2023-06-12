#!/usr/bin/python3
""" a class that defines all common attributes/methods for other classes """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ the base class for all other classes in this project """
    def __init__(self, *args, **kwargs):
        if kwargs:
                if "__class__" in kwargs:
                    del kwargs["__class__"]
                for key, value in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """represent func in string format"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """save and update uuid"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """represent instance in dict format"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat("T", "microseconds")
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat("T", "microseconds")
        return obj_dict
