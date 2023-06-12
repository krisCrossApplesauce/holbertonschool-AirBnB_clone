#!/usr/bin/python3
""" a class called User that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
