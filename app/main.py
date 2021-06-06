# framework packages
from fastapi import FastAPI

# local packages
from app import routers, database, models

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(routers.endpoint.auth.router,
                   prefix="/api/v1/auth", tags=["auth"])
app.include_router(routers.endpoint.users.router,
                   prefix="/api/v1/users", tags=["users"])
app.include_router(routers.endpoint.countries.router,
                   prefix="/api/v1/countries", tags=["countries"])
