from app.models import Address
from typing import List, Optional
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


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class BaseRequest(BaseModel):
    pass


class UserRegisterRequest(BaseRequest, UserBase):
    password: str


class UserLoginRequest(BaseRequest, UserBase):
    password: str


class BaseResponse(BaseModel):
    success: bool


class UserResponse(BaseResponse):
    user: User


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
