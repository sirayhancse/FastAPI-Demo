from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from app import models, schemas


class Countries():

    def __init__(self, db) -> None:
        self.db: Session = db

    def create_country(self, user_id: int, country: schemas.CreateCountry):
        country_obj = models.Country(name=country.name,
                                     latitude=country.latitude,
                                     longitude=country.longitude,
                                     code=country.code,
                                     owner_id=user_id
                                     )
        self.db.add(country_obj)
        self.db.flush()

        for state in country.states:
            state_obj = models.State(
                name=state.name, country_id=country_obj.id
            )
            self.db.add(state_obj)
            self.db.flush()

            for address in state.addresses:
                address_obj = models.Address(
                    name=address.name,
                    house_number=address.house_number,
                    road_number=address.road_number,
                    state_id=state_obj.id
                )
            self.db.add(address_obj)

        return country_obj

    def get_countries(self, country_name, country_code, skip, limit):

        if country_name and country_code:
            return self.db.query(models.Country).filter(
                and_(models.Country.name.ilike(str(country_name)),
                     models.Country.code.ilike(str(country_code))
                     )).offset(skip).limit(limit).all()

        elif country_name or country_code:
            return self.db.query(models.Country).filter(
                or_(models.Country.name.ilike(str(country_name)),
                    models.Country.code.ilike(str(country_code))
                    )).offset(skip).limit(limit).all()
        else:
            return self.db.query(models.Country).offset(skip).limit(limit).all()

    def get_states_by_country(self, country_id, state_name, skip, limit):

        if state_name:
            return self.db.query(models.State).filter(
                models.State.country_id == country_id,
                models.State.name.ilike(str(state_name))
            ).offset(skip).limit(limit).all()
        else:
            return self.db.query(models.State).filter(
                models.State.country_id == country_id
            ).offset(skip).limit(limit).all()

    def get_addresses_by_state(self, state_id, house_number, road_number, skip, limit):

        if house_number and road_number:
            return self.db.query(models.Address).filter(
                models.Address.state_id == state_id,
                models.Address.house_number.ilike(str(house_number)),
                models.Address.road_number == road_number
            ).offset(skip).limit(limit).all()

        elif house_number or road_number:
            return self.db.query(models.Address).filter(
                models.Address.state_id == state_id,
                or_(models.Address.house_number.ilike(str(house_number)),
                    models.Address.road_number == road_number)
            ).offset(skip).limit(limit).all()

        else:
            return self.db.query(models.Address).filter(
                models.Address.state_id == state_id
            ).offset(skip).limit(limit).all()

    def get_address_details(self, address_name):
        return self.db.query(models.Address, models.State, models.Country).filter(
            models.Country.id == models.State.country_id
        ).filter(
            models.State.id == models.Address.state_id
        ).filter(
            models.Address.name.ilike(str(address_name))
        ).first()

    def is_country_exist(self, user_id: int, country_name: str):
        return bool(self.db.query(models.Country).filter(
            models.Country.owner_id == user_id,
            models.Country.name == country_name
        ).first())
