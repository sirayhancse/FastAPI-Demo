from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from app import models, schemas


class Countries():

    def __init__(self, db) -> None:
        self.db: Session = db

    def create_country(self, country: schemas.CreateCountry):
        country_obj = models.Country(name=country.name,
                                     latitude=country.latitude,
                                     longitude=country.longitude,
                                     code=country.code
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
