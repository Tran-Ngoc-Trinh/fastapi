from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///sales.db'
# connect_args: chỉ dùng cho sqlite
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal: mở kết nối để thêm - xoá - sửa
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind = engine)

Base = declarative_base()