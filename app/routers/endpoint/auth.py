import os

from fastapi import Request, APIRouter, Depends, HTTPException, status
from fastapi.applications import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from app import schemas, auth
from app.crud.db.users import Users as CrudUser
from app.utils import get_db

from app.config import settings

app = FastAPI()

router = InferringRouter()


@cbv(router)
class Auth():
    db: Session = Depends(get_db)

    @router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
    def register(self, user: schemas.UserRegisterRequest):
        db_users = CrudUser(db=self.db)
        user_data = db_users.get_user_by_email(email=user.email)
        if user_data:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Email already registered")
        registered_user = db_users.create_user(user=user)

        return {
            "success": True,
            "user": registered_user
        }

    def authenticate_user(self, username: str, password: str):
        db_users = CrudUser(db=self.db)
        user = db_users.get_user_by_email(email=username)
        if not user or not auth.verify_password(password, user.hashed_password):
            return False
        return user

    @router.post("/login", response_model=schemas.Token)
    async def login(self, form_data: OAuth2PasswordRequestForm = Depends()):
        user = self.authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"}
            )
        access_token = auth.create_access_token(data={"sub": user.email})
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
