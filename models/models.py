""" dict of existing models """

"""
IMPORT ALL THE STUFF NEEDED FOR A DICT
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User

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
