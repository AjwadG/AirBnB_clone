#!/usr/bin/python3
''' file storage module '''
import json
from models.base_model import BaseModel


class FileStorage(object):
    ''' serializes and deserializes objects to
        and from json files
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dic of the class
        '''
        return self.__objects

    def new(self, obj):
        ''' sets in __object the obj
            with the key <class name>.<id>
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        ''' saves the object to a json file '''
        new_obj = {}
        for key, value in self.__objects.items():
            new_obj[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_obj, file)

    def reload(self):
        ''' reloads the object from a json file '''
        try:
            with open(self.__file_path, 'r') as file:
                file_content = json.load(file)
                for key, value in file_content.items():
                    print(value)
                    self.__objects.update({key: value})
        except FileNotFoundError:
            pass
