from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class Article():
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    magazine_id = Column(Integer, ForeignKey('magazines.id'))
    magazine = relationship("Magazine", backref=backref('articles', order_by=id))
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer")
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        """
        Set the title of the article.

        Parameters:
        value (str): The new title of the article.

        Raises:
        ValueError: If the title is not a string or its length is less than 5 or more than 50 characters.

        Returns:
        None
        """
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value


    def __repr__(self):
        return f"Article('{self.title}', {self.author.id}, {self.magazine.id})"
    
    def author(self):
        return self.author


    def magazine(self):
        return self.magazine


    def articles(self):
        return self.magazine.articles


    def magazines(self):
        return self.author.magazines


    def article_titles(self):
       articles = self.magazine.articles
       titles = [article.title for article in articles]
       return titles if articles else None


    def contributing_authors(self):
        authors = self.magazine.authors
        contributors = [author for author in authors if len(author.articles) > 2]
        return contributors if authors else None
    