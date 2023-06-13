#!/usr/bin/python3
"""
    Module for Review model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        public class attributes:
            place_id: string or empty string (Place.id)
            user_id: string or empty string (User.id)
            text: string or empty string
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(Review, self).to_dict()
