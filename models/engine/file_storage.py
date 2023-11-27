#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        if cls is None:
            return FileStorage.__objects
        return {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            temp = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(temp, f)

    def delete(self, obj=None):
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                from models.base_model import BaseModel
                from models.user import User
