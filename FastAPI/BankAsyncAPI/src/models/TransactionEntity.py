import uuid
from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from FastAPI.BankAsyncAPI.src.models.AccountEntity import AccountEntity
from FastAPI.BankAsyncAPI.src.models.BaseModel import BaseModel

class TransactionEntity(BaseModel):
    __tablename__ = "transactions"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount: Mapped[float] = mapped_column(Float(), nullable=False)
    from_account: Mapped[AccountEntity] = relationship("AccountEntity")
    from_account_id: Mapped[uuid] = mapped_column(ForeignKey("accounts.pk_id"))
    to_account: Mapped[AccountEntity] = relationship("AccountEntity")
    to_account_id: Mapped[uuid] = mapped_column(ForeignKey("accounts.pk_id"))