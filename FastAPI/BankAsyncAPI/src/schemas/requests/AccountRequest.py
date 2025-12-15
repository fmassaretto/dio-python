from typing import Annotated

from pydantic import Field
from FastAPI.BankAsyncAPI.src.schemas import BaseSchema
from FastAPI.BankAsyncAPI.src.schemas.requests import ClientRequest


class AccountRequest(BaseSchema):
    agency_number: Annotated[str, Field(description="Numero da agencia", examples="0001", max_length=4)]
    account_number: Annotated[str, Field(description="Numero da conta", examples="12345-09", max_length=8)]
    balance: Annotated[float, Field(description="quantidade de dinheiro", examples="1000,00")]
    client: Annotated[ClientRequest, Field(description="Cliente responsavel pela conta", examples="Joao Silva")]