#!/usr/bin/python3
"""module: Amenity model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        public class attributes:
            name: string or empty string
    """


    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(Amenity, self).to_dict()
