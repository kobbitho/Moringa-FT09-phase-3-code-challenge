from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
class Author():
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name
        

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value


    def __repr__(self):
        return f"Author('{self.name}`)"
    
    def articles(self):
        return self.articles
    
    def magazines(self):
        return self.magazines
    