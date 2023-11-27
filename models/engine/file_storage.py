#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        return {k: v for k, v in FileStorage.__objects.items()
                if isinstance(v, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        """Adds a new object to the storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        """Saves the storage dictionary to a file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Delets obj of __objects if it is inside """
        """Deletes obj from __objects if it is inside"""
        if not obj:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        del FileStorage.__objects[key]

    def reload(self):
        """Loads storage dictionary from file"""
        """Loads the storage dictionary from a file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        def reload(self):
        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
def delete(self, obj=None):
        """Function removes an object from the __objects dictionary within an instance of a class."""
        if obj is not None:
            key = f"{obj.__class__.__name__ }.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
