#!usr/bin/python3
# base model to for children to inherit

import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for all models
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # formatting the string
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    # save for main model
    def save(self):
        """
        Saves and updates the state of the base model
        """
        self.updated_at = datetime.now()

    #converts the object to a dictionary
    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
