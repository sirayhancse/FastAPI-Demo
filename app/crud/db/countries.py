from sqlalchemy.orm import Session

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
