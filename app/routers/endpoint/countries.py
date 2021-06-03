from fastapi import FastAPI, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from ...utils import get_db
from app import schemas


app = FastAPI()
router = InferringRouter()



@cbv(router)
class Countries():
    db: Session = Depends(get_db)

    @router.post("/")
    def create_country(self, country: schemas.CreateCountry):
        return country

    @router.get("/")
    def get_all_countries(self):
        return {"name": "Bangladesh"}

app.include_router(router)
