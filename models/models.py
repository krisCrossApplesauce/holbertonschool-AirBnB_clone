""" dict of existing models """

"""
IMPORT ALL THE STUFF NEEDED FOR A DICT
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.State import State
from models.Place import Place
from models.Review import Review
from models.User import User

"""
model dictionary here
"""
models_dict = {
    ("BaseModel", BaseModel),
    ("Amenity", Amenity),
    ("City", City),
    ("State", State),
    ("Place", Place),
    ("Review", Review),
    ("User", User)
}
