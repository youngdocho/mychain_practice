from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine('sqlite:///mychain.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = scoped_session(sessionmaker(bind=engine))
session = DBSession()


def init():
    Base.metadata.create_all(engine)

# http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#create-an-instance-of-the-mapped-class
def insert(obj):
    # todo
    return


def insert_or_update(obj, cond):
    # todo
    return
# return mandatory


def get(clz, **kwargs):
    # todo
    return
# return mandatory


def count(clz):
    # todo
    return
# return mandatory


def remove(obj):
    # todo
    return


def get_all(clz):
    # todo
    return
# return mandatory


def remove_all(clz):
    # todo
    return
