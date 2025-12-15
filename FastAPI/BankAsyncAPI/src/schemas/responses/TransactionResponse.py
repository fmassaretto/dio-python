
from typing import Annotated

from pydantic import Field
from FastAPI.BankAsyncAPI.src.schemas.responses import AccountResponse


class TransactionEntity():
    amount: Annotated[float, Field(description="Quantidade de dinheiro", examples="1000,00")]
    from_account: Annotated[AccountResponse, Field(description="Conta do cliente remetente")]
    to_account: Annotated[AccountResponse, Field(description="Conta do cliente destinatario")]