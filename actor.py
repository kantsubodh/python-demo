# coding=utf-8

from sqlalchemy import Column, String, Integer, Date
from base import Base


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    birthday = Column(Date)

    def __init__(self, id, name, birthday):
        self.id = id
        self.name = name
        self.birthday = birthday