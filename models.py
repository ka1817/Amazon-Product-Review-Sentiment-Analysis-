from sqlalchemy import Column, Integer, String, Text, Float
from database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    sentiment = Column(String, nullable=False)  # 'positive' or 'negative'
    confidence = Column(Float, nullable=False)  # Model confidence score
