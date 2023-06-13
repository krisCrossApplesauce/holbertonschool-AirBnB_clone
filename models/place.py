#!/usr/bin/python3
"""
    Module for Place model
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        public class attributes:
            city_id: string or empty string (City.id)
            user_id: string or empty string (User.id)
            name: string or empty string
            description: string or empty string
            number_rooms: integer - 0
            number_bathrooms: integer - 0
            max_guest: integer - 0
            price_by_night: integer - 0
            latitude: float - 0.0
            longitude: float - 0.0
            amenity_ids: list of strings or empty list (eventually amenity.id)
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(Place, self).to_dict()
