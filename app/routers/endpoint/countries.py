from fastapi import FastAPI, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

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

    @router.get("/")
    def get_all_countries(self):
        return {"name": "Bangladesh"}

app.include_router(router)
