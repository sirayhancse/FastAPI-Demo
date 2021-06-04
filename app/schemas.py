from app.models import Address
from typing import List
from pydantic import BaseModel


class AddressBase(BaseModel):
    name: str
    house_number: str
    road_number: int


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True


class StateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class State(StateBase):
    id: int

    class Config:
        orm_mode = True


class CountryBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    code: str

    class Config:
        orm_mode = True


class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True


class StateAdress(StateBase):
    addresses: List[AddressBase]


class CreateCountry(CountryBase):
    states: List[StateAdress]


class AddressDetails(Address):
    state: StateBase
    country: CountryBase
