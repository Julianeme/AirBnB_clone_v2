#!/usr/bin/python3
""" Data base Storage.

"""
import models
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from os import getenv


class DBStorage():
    """ This class create the connection between mysql+mysqldb,
    with the methods init, all, new, save and reload.

    """
    __engine = None
    __session = None

    def __init__(self):
        """ This method create the enigne.

        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB'),
            pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ This method create the query to the class (cls) and
        if is none create the query to all the classes.
        Return: the object in form of dictionary.

        """
        from ..state import State
        from ..city import City
        from ..user import User
        from ..review import Review
        from ..place import Place
        my_dict = {}
        if cls is not None:
            for obj in self.__session.query(cls):
                key_obj = obj.__class__.__name__ + '.' + obj.id
                my_dict[key_obj] = obj
        else:
            my_list = [User, State, City, Place, Review]
            for _list in my_list:
                for obj in self.__session.query(_list):
                    key_obj = obj.__class__.__name__ + '.' + obj.id
                    my_dict[key_obj] = obj
        return my_dict

    def new(self, obj):
        """ This method add an new object.

        """
        self.__session.add(obj)

    def save(self):
        """ This method save the object.

        """
        self.__session.commit()

    def delete(self, obj=None):
        """ This method delete a object.

        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ This method create all tables of the data base and log in.

        """
        from ..state import State, Base
        from ..city import City
        from ..user import User
        from ..place import Place
        from ..review import Review
        from ..amenity import Amenity
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            expire_on_commit=False, bind=self.__engine))
