#!/usr/bin/python3
from os import environ
from sqlalchemy import create_engine, text
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation od database """
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db}',
            pool_pre_ping=True)

    def all(self, cls=None):
        """ Returns a dict of the specified cls """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'State': State,
            'City': City,
            'User': User,
            'Place': Place,
            'Amenity': Amenity,
            'Review': Review
        }

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        dic = {}

        # if a cls argument is provided
        if cls:
            if type(cls) is not str:
                cls = cls.__name__
            for obj in self.__session.query(classes[cls]):
                dic[str(cls) + '.' + obj.id] = obj
        else:
            for k in classes.keys():
                for obj in self.__session.query(classes[k]):
                    dic[str(k) + '.' + obj.id] = obj
        return dic

    def new(self, obj):
        """ Add a new object to the data base """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reload all the objets """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        smk = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(smk)

    def close(self):
        """ Close the session """
        self.__session.close()
