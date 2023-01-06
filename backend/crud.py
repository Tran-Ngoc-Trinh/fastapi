from sqlalchemy.orm import Session
import models as models
import schemas as schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    result = db.query(models.User).all()
    return result

def get_user(db: Session, user_id: int):
    result = db.query(models.User).filter(models.User.id == user_id).first()
    return result

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def checkLogin(db: Session,email: str, password: str):
    return db.query(models.User).filter(models.User.email == email and models.User.password == password).first()

def create_user(db: Session, user: schemas.User):
    db_user = models.User(username= user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user