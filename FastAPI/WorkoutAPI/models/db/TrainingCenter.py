from sqlalchemy import Integer, String
from FastAPI.WorkoutAPI.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TrainingCenter(BaseModel):
    __tablename__ = "training_centers"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String(60), nullable=False)
    owner: Mapped[str] = mapped_column(String(30), nullable=False)
    athlete: Mapped["Athlete"] = relationship(back_populates="training_center")