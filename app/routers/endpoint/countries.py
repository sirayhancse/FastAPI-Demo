from re import L
from fastapi import FastAPI, Depends, Query
from fastapi.param_functions import Path
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
                          limit: Optional[str] = Query(10, alias="limit")
                          ):

        service_countries = CountriesService()

        return service_countries.get_countries(db=self.db,
                                               country_name=country_name,
                                               country_code=country_code,
                                               skip=skip,
                                               limit=limit
                                               )

    @router.get("/{country_id}/states", response_model=List[schemas.State])
    def get_states_by_country(self, country_id: int,
                              state_name: Optional[str] = Query(
                                  "", alias="state-name"),
                              skip: Optional[str] = Query(0, alias="skip"),
                              limit: Optional[str] = Query(10, alias="limit")
                              ):

        service_countries = CountriesService()

        return service_countries.get_states_by_country(db=self.db,
                                                       country_id=country_id,
                                                       state_name=state_name,
                                                       skip=skip,
                                                       limit=limit
                                                       )

    @router.get("/states/{state_id}/addresses", response_model=List[schemas.Address])
    def get_addresses_by_state(self, state_id: int,
                              house_number: Optional[str] = Query(
                                  "", alias="house-name"),
                              road_number: Optional[str] = Query(
                                  None, alias="road-number"),
                              skip: Optional[str] = Query(0, alias="skip"),
                              limit: Optional[str] = Query(10, alias="limit")
                              ):

        service_countries = CountriesService()

        return service_countries.get_addresses_by_state(db=self.db,
                                                        state_id=state_id,
                                                        house_number=house_number,
                                                        road_number=road_number,
                                                        skip=skip,
                                                        limit=limit
                                                        )


app.include_router(router)
