from datetime import datetime
from sqlalchemy import DateTime, Integer, String
from models.BaseModel import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TrainingCenter(BaseModel):
    __tablename__ = "training_centers"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String(60), nullable=False)
    owner: Mapped[str] = mapped_column(String(30), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    athlete: Mapped["Athlete"] = relationship(back_populates="training_center")