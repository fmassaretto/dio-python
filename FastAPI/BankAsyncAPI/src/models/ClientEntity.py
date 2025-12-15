from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from FastAPI.BankAsyncAPI.src.models.AccountEntity import AccountEntity
from FastAPI.BankAsyncAPI.src.models import AccountEntity
from FastAPI.BankAsyncAPI.src.models.BaseModel import BaseModel

class ClientEntity(BaseModel):
    __tablename__ = "clients"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=False)
    account: Mapped[AccountEntity] = relationship("AccountEntity", back_populates="cliententity", lazy="selectin")
