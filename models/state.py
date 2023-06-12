#!/usr/bin/python3
"""
    module: state model
"""
from models.base_model import BaseModel


class State(BaseModel):

    """
    public class attributes:
            name: string or empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(State, self).to_dict()
