import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)
    username = Column(String(16), unique=True)
    firts_name = Column(String(60))
    last_name = Column(String(60))
    password = Column(String(50))
    #Relations
    posts = relationship("Post", backref="user")
    comments = relationship("Comment", backref="user")
    post_likes = relationship("PostLike", backref="user")
    comment_likes = relationship("CommentLike", backref="user")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table post.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    image_url = Column(String(250), unique=True)
    date_published = Column(DateTime())
    content = Column(String(300), nullable=False)
    latittude = Column(String(150), nullable=False)
    longitude = Column(String(150), nullable=False)
    #Relations
    comments = relationship("Comment", backref="post")
    post_likes = relationship("PostLike", backref="post")

class PostLike(Base):
    __tablename__ = 'postlike'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    content = Column(String(300))
    date_time = Column(DateTime())
    #Relations
    comment_likes = relationship('CommentLike', backref="comment")

class CommentLike(Base):
    __tablename__ = 'commentlike'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')