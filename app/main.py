#framework packages
from fastapi import FastAPI

#local packages
from app import routers


app = FastAPI()

app.include_router(routers.endpoint.countries.router, prefix="/api/v1/countries", tags=["countries"])
