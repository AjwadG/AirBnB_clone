#!/usr/bin/python3
''' amenity module '''
from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' Amenity Model '''
    name: str = ""
