from typing import Annotated

from pydantic import Field

from FastAPI.BankAsyncAPI.src.schemas import BaseSchema
from FastAPI.BankAsyncAPI.src.schemas.requests import AccountRequest

class TransactionRequest(BaseSchema):
    amount: Annotated[float, Field(description="Quantidade de dinheiro", examples="1000,00")]
    from_account: Annotated[AccountRequest, Field(description="Conta do cliente remetente")]
    to_account: Annotated[AccountRequest, Field(description="Conta do cliente destinatario")]