from fastapi import HTTPException, status
from typing import Optional

from fastapi.encoders import jsonable_encoder

from ... import schemas
from app.crud.db.countries import Countries as CountriesCrud


class Countries():

    def create_country(self, db, country: schemas.CreateCountry):
        db_countries = CountriesCrud(db=db)
        is_exist = db_countries.is_country_exist(country.name)
        if not is_exist:
            country_obj = db_countries.create_country(country=country)
            if country_obj:
                db.commit()
                raise HTTPException(status_code=status.HTTP_201_CREATED,
                                    detail="Country created successfully")
            else:
                raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                    detail="Country created failed")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Country already exists")

    def get_countries(self, db, country_name, country_code, skip, limit):
        db_countries = CountriesCrud(db=db)

        country_list = db_countries.get_countries(
            country_name=country_name,
            country_code=country_code,
            skip=skip,
            limit=limit
        )

        if country_list:
            return country_list
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No country found")

    def get_states_by_country(self, db, country_id, state_name, skip, limit):
        db_countries = CountriesCrud(db=db)

        state_list = db_countries.get_states_by_country(
            country_id=country_id,
            state_name=state_name,
            skip=skip,
            limit=limit
        )

        if state_list:
            return state_list
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No states found")

    def get_addresses_by_state(self, db, state_id, house_number, road_number, skip, limit):
        db_countries = CountriesCrud(db=db)

        address_list = db_countries.get_addresses_by_state(
            state_id=state_id,
            house_number=house_number,
            road_number=road_number,
            skip=skip,
            limit=limit
        )

        if address_list:
            return address_list
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No address found")

    def get_addresses_details(self, db, address_name):
        db_countries = CountriesCrud(db=db)

        address_details = db_countries.get_address_details(
            address_name=address_name
        )

        if address_details:
            return {
                "id": address_details.Address.id,
                "name": address_details.Address.name,
                "house_number": address_details.Address.house_number,
                "road_number": address_details.Address.road_number,
                "state": address_details.State,
                "country": address_details.Country
            }
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No address found")
