from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from FastAPI.WorkoutAPI.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Athlete(BaseModel):
    __tablename__ = "athletes"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    height: Mapped[float] = mapped_column(Float, nullable=False)
    sex: Mapped[str] = mapped_column(String(1), nullable=False)
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    category: Mapped["Category"] = relationship(back_populates="athlete")
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.pk_id"))
    training_center: Mapped["TrainingCenter"] = relationship(back_populates="athlete")
    training_cente_id: Mapped[int] = mapped_column(ForeignKey("training_centers.pk_id"))