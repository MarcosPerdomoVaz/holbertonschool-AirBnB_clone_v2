#!/usr/bin/python3
"""This is the DB storage engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv

class DBStorage:
    """DBStorage class for working with the MySQL database."""
    __engine = None
    __session = None

    def __init__(self):
        """Create a new instance of DBStorage."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects from the current database session."""
        result = {}
        if cls:
            query_result = self.__session.query(cls).all()
        else:
            classes = [City, State]  # Add other classes as needed
            query_result = []
            for c in classes:
                query_result += self.__session.query(c).all()
        for obj in query_result:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            result[key] = obj
        return result

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session."""
        self.__session.remove()
