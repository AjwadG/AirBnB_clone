#!/usr/bin/python3
''' file storage module '''
import json
from models.base_model import BaseModel

models = {"BaseModel": BaseModel}


class FileStorage(object):
    ''' serializes and deserializes objects to
        and from json files
    '''
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
            with open(self.__file_path, 'r') as file:
                file_content = json.load(file)
                for key, value in file_content.items():
                    self.__objects[key] = models[value["__class__"]](**value)
        except FileNotFoundError:
            pass
