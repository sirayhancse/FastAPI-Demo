from fastapi import FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter


app = FastAPI()
router = InferringRouter()



@cbv(router)
class Countries():
    @router.get("/")
    def get_all_countries(self):
        return {"name": "Bangladesh"}

app.include_router(router)
