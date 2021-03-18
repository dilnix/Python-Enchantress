from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import INTEGER
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Time


Base = declarative_base()
metadata = Base.metadata


class Owner(Base):
    __tablename__ = 'owner'

    id = Column(INTEGER, primary_key=True)
    name = Column(String(50))
    phone = Column(String(50), unique=True)
