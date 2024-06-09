from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
class Magazine():
    __tablename__ = 'magazines'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    articles = relationship("Article", backref=backref('magazines', order_by=id))
    authors = relationship("Author", secondary='magazine_authors', backref=backref('magazines', order_by=id))
    
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

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

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def __repr__(self):
        return f"Magazine('{self.name}', {self.id}, '{self.category}')"
    
    def articles(self):
        return self.articles

    def contributors(self):
        return self.authors