from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship


from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    countries = relationship("Country", back_populates="owner")


class Country(Base):

    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)
    code = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="countries")
    states = relationship("State", back_populates="country")


class State(Base):

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    country_id = Column(Integer, ForeignKey("countries.id"))

    country = relationship("Country", back_populates="states")

    addresses = relationship("Address", back_populates="state")


class Address(Base):

    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    house_number = Column(String, index=True)
    road_number = Column(Integer, index=True)
    state_id = Column(Integer, ForeignKey("states.id"))

    state = relationship("State", back_populates="addresses")
