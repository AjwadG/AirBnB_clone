#!/usr/bin/python3
''' BaseModel class module '''
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    ''' base model for all '''
    def __init__(self, *args, **kwargs):
        ''' initing instance attributes '''
        if kwargs and len(kwargs) != 0:
            tf = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], tf)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], tf)
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        ''' returining string rep of the obj '''
        name = self.__class__.__name__
        cid, dic = self.id, self.__dict__
        return "[{}] ({}) {}".format(name, cid, dic)

    def save(self):
        ''' updates the updated_at attribute'''
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        ''' dic of the class '''
        dic = self.__dict__
        dic["updated_at"] = dic["updated_at"].isoformat()
        dic["created_at"] = dic["created_at"].isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
