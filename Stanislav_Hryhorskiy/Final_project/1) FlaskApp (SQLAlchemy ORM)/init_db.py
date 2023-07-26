from sqlalchemy import create_engine, Column, Integer, String, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine(r"sqlite:///database_new.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Post(Base):
    """
    A class representing a blog post.

    Attributes:
        id (int): The unique identifier of the post.
        created (str): The creation date of the post in the format DD-MM-YY HH:MM:SS.
        title (str): The title of the post.
        content (str): The content of the post.
    """
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(String(19), nullable=False)
    title = Column(UnicodeText(100), nullable=False)
    content = Column(String(1000), nullable=False)


Base.metadata.create_all(engine)

