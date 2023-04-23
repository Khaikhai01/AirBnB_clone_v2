#!/iusr/bin/python3
""" database storage management """
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

user = os.environ.get('HBNB_MYSQL_USER')
password = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
database = os.environ.get('HBNB_MYSQL_DB')


class DBStorage():
    """ a class defining methods and attributes for the database """

    __engine = None
    __session = None

    def __init__(self):
        """ initiliazes the class """
        DBStorage.__engine = create_engine(
             f'mysql+mysqldb://{user}:{password}@{host}/{database}',
             pool_pre_ping=True
        )
        hbnd_env = os.environ.get('HBNB_ENV')
        if (hbnd_env == "test"):
            Base.metadata.drop_all(DBStorage.__engine)

    def all(self, cls=None):
        """ retrives all objects """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Session = sessionmaker(bind=DBStorage.__engine)
        DBStorage.__session = Session()
        objects = {}
        if cls is not None:
            # Query for objects of a specific class
            results = DBStorage.__session.query(cls).all()
        else:
            # Query for all types of objects
            results = []
            for cls in [State, City, User, Place, Review, Amenity]:
                results.extend(DBStorage.__session.query(cls).all())
        # Add objects to dictionary
        for obj in results:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objects[key] = obj
        DBStorage.__session.close()
        return objects

    def new(self, obj):
        """ add a new object to the session """

        DBStorage.__session.add(obj)

    def save(self):
        """ saves an object to the database """

        DBStorage.__session.commit()

    def delete(self, obj=None):
        """ deletes an object from current session """
        if (obj):
            DBStorage.__session.delete(obj)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        # create all tables in the database
        Base.metadata.create_all(DBStorage.__engine)

        # create the current database session
        session_factory = sessionmaker(
            bind=DBStorage.__engine,
            expire_on_commit=False
        )
        DBStorage.__session = scoped_session(session_factory)

    def close(self):
        '''closing session'''
        DBStorage.__session.close()
