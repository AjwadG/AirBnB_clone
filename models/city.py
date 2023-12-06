#!/usr/bin/python3
''' city module '''
from models.base_model import BaseModel


class City(BaseModel):
    ''' City Model '''
    state_id: str = ""
    name: str = ""
