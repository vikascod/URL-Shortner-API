from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
import datetime


class TinyURL(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    original_url = Column(String, unique=True)
    tiny_url = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.now())