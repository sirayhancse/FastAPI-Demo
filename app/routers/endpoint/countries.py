from re import L
from fastapi import FastAPI, Depends, Query
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session
from typing import Optional, List

from ...utils import get_db
from app import schemas
from app.services.db.countries import Countries as CountriesService


app = FastAPI()
router = InferringRouter()


@cbv(router)
class Countries():
    db: Session = Depends(get_db)

    @router.post("/")
    def create_country(self, country: schemas.CreateCountry):
        service_countries = CountriesService()

        return service_countries.create_country(db=self.db, country=country)

    @router.get("/", response_model=List[schemas.Country])
    def get_all_countries(self, country_name: Optional[str] = Query("", alias="country-name"),
                          country_code: Optional[str] = Query(
                              "", alias="country-code"),
                          skip: Optional[str] = Query(0, alias="skip"),
                          limit: Optional[str] = Query(10, alias="limit")):
        service_countries = CountriesService()

        return service_countries.get_countries(db=self.db,
                                               country_name=country_name,
                                               country_code=country_code,
                                               skip=skip,
                                               limit=limit
                                               )


app.include_router(router)
