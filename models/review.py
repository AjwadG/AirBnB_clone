#!/usr/bin/python3
''' review module '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Review Model '''
    place_id: str = ""
    user_id: str = ""
    text: str = ""
