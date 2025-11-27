from datetime import datetime
from sqlalchemy import DateTime, Integer, String
from models.BaseModel import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Category(BaseModel):
    __tablename__ = "categories"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    athlete: Mapped["Athlete"] = relationship("Athlete", back_populates="category")