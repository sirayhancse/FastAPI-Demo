import re
from fastapi import APIRouter, Depends
from fastapi.applications import FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm.session import Session

from app import schemas, auth
from app.utils import get_db

app = FastAPI()
router = InferringRouter()


@cbv(router)
class Users():
    db: Session = Depends(get_db)

    @router.get("/me", response_model=schemas.UserResponse)
    def get_current_active_user(self, user: schemas.User = Depends(auth.get_current_active_user)):
        """
        Get details of authenticated user
        """
        print(user)
        return {
            "success": True,
            "user": user
        }
