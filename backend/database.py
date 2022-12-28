from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
# from .config import settings

config = dotenv_values("./.env")
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{config.get('MYSQL_ROOT_USER')}:{config.get('MYSQL_ROOT_PASSWORD')}@{config.get('MYSQL_HOSTNAME')}:{config.get('DATABASE_PORT')}/{config.get('MYSQL_DATABASE')}"
# connect_args: chỉ dùng cho sqlite
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal: mở kết nối để thêm - xoá - sửa
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind = engine)

Base = declarative_base()