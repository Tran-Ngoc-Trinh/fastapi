from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config = dotenv_values("../.env")
# connect_args: chỉ dùng cho sqlite
engine = create_engine(config.get('POSTGRESQL_DATABASE_CONNECTION_URL'))
# SessionLocal: mở kết nối để thêm - xoá - sửa
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind = engine)

Base = declarative_base()