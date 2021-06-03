from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship


from .database import Base


class Country(Base):

    __tablename__ = "countries"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)
    code = Column(String, index=True)

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