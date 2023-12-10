#!/usr/bin/python3
''' city module '''
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    state_id: str = ""
    name: str = ""
