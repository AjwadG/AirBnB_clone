#!/usr/bin/python3
''' file storage module '''
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

models = {"BaseModel": BaseModel, "User": User, "State": State,
          "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage(object):
    """FILE storage engine.

    Attributes:
        __file_path (str): path of the file to save objects to.
        __objects (dict): A dictionary of objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dic of the class
        '''
        return FileStorage.__objects

    def new(self, obj):
        ''' sets in __object the obj
            with the key <class name>.<id>
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        ''' saves the object to a json file '''
        new_obj = {}
        for key in FileStorage.__objects:
            new_obj[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_obj, file)

    def reload(self):
        ''' reloads the object from a json file '''
        try:
            with open(FileStorage.__file_path, 'r') as file:
                file_content = json.load(file)
                for key, value in file_content.items():
                    obj = models[value["__class__"]](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
