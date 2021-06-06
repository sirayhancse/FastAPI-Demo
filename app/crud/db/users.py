from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from app import models, schemas, auth


class Users():

    def __init__(self, db) -> None:
        self.db: Session = db

    def create_user(self, user: schemas.UserRegisterRequest):
        hashed_password = auth.get_password_hash(user.password)
        create_user = models.User(email=user.email,
                                  hashed_password=hashed_password
                                  )
        self.db.add(create_user)
        self.db.commit()
        return create_user

    def get_user_by_id(self, user_id: int):
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(models.User).filter(models.User.email == email).first()

    def get_all_user(self):
        return {
            "success": True,
            "users": self.db.query(models.User).all()
        }
