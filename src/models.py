import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class User(Base):
    __tablename__ ='user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique= True, nullable=False)
    password = Column(String(50), nullable=False)

class Login(Base):
    __tablename__ = 'logins'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    user= relationship("User",back_populates="logins")
                     

     
    
class Character(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    description = Column(String(250), nullable=False)
    planet_id =  Column(Integer,ForeignKey("planets.id"),nullable=True)


class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable=False)
    name = Column(String(25), nullable=False)
    description = Column(String(250), nullable=False)
    terrain = Column(String(100), nullable=False)

    characters = relationship("Character",backref="planet")

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer,ForeignKey("users.id"),nullable=False)
    character_id= Column(Integer,ForeignKey("characters.id"),nullable=False)
    planet_id= Column(Integer,ForeignKey("planets.id"),nullable=False)

    character = relationship("Character",backref="favorite") 
    planet = relationship("Planet",backref="favorite")
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
