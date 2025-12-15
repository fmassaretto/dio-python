from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from FastAPI.BankAsyncAPI.src.models.BaseModel import BaseModel
from FastAPI.BankAsyncAPI.src.models.ClientEntity import ClientEntity


class AccountEntity(BaseModel):
    __tablename__ = "accounts"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    agency_number: Mapped[str] = mapped_column(String(5), nullable=False)
    account_number: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    balance: Mapped[float] = mapped_column(Float)
    client: Mapped[ClientEntity] = relationship("ClientEntity", back_populates="accountentity")
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.pk_id"))