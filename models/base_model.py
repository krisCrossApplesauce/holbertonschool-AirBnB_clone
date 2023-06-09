#!/usr/bin/python3
""" a class that defines all common attributes/methods for other classes """
import uuid
import datetime


class BaseModel:
    """ the base class for all other classes in this project """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
