from fastapi import HTTPException, status
from typing import Optional

from ... import schemas
from app.crud.db.countries import Countries as CountriesCrud


class Countries():

    def create_country(self, db, country: schemas.CreateCountry):
        db_countries = CountriesCrud(db=db)

        country_obj = db_countries.create_country(country=country)

        if country_obj:
            db.commit()
            raise HTTPException(status_code=status.HTTP_201_CREATED,
                                detail="Country created successfully")
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="Country created failed")

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
