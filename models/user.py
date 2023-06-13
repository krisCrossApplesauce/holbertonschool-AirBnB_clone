#!/usr/bin/python3
"""
a class called User that inherits from BaseModel
public class attributes:
email: string or empty
password: string or empty
first_name: string or empty
last_name: string or empty
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
