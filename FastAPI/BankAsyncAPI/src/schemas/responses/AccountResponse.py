from typing import Annotated

from pydantic import Field
from FastAPI.BankAsyncAPI.src.models import ClientEntity


class AccountResponse():

    agency_number: Annotated[str, Field(description="Numero da agencia", examples="0001", max_length=4)]
    account_number: Annotated[str, Field(description="Numero da conta", examples="12345-09", max_length=8)]
    balance: Annotated[float, Field(description="quantidade de dinheiro", examples="1000,00")]
    client: Annotated[ClientEntity, Field(description="Cliente responsavel pela conta", examples="Joao Silva")]