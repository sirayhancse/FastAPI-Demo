from fastapi import HTTPException, status
from typing import Optional

from fastapi.encoders import jsonable_encoder

from ... import schemas
from app.crud.db.countries import Countries as CountriesCrud


class Countries():

    def create_country(self, db, user_id: int, country: schemas.CreateCountry):
        db_countries = CountriesCrud(db=db)
        is_exist = db_countries.is_country_exist(
            user_id=user_id, country_name=country.name)
        if not is_exist:
            country_obj = db_countries.create_country(
                user_id=user_id, country=country)
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

    def get_countries(self, db, user_id: int, country_name: str,
                      country_code: str, skip: int, limit: int):
        db_countries = CountriesCrud(db=db)

        country_list = db_countries.get_countries(
            user_id=user_id,
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

    def get_states_by_country(self, db, user_id: int, country_id: int,
                              state_name: str, skip: int, limit: int):
        db_countries = CountriesCrud(db=db)

        state_list = db_countries.get_states_by_country(
            user_id=user_id,
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

    def get_addresses_by_state(self, db, user_id: int, state_id: int,
                               house_number: str, road_number: str, skip: int, limit: int):
        db_countries = CountriesCrud(db=db)

        address_list = db_countries.get_addresses_by_state(
            user_id=user_id,
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

    def get_addresses_details(self, db, user_id: int, address_name: str):
        db_countries = CountriesCrud(db=db)

        address_details = db_countries.get_address_details(
            user_id=user_id,
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
