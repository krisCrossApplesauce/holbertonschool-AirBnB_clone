#!/usr/bin/python3
"""
    module: Cities model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        public class attributes:
            state_id: string or empty string (will be the state.id)
            name: string or empty string
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(City, self).to_dict()
