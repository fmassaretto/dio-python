from typing import Annotated

from pydantic import Field
from FastAPI.BankAsyncAPI.src.schemas.BaseSchema import BaseSchema

class ClientRequest(BaseSchema):
    name: Annotated[str, Field(description="Nome do cliente", examples="Joao Silva", max_length=50)]
    email: Annotated[str, Field(description="Email do cliente", examples="joao@email.com", max_length=80)]
    phone: Annotated[str, Field(description="Telefone do cliente", examples="+55(11)91234-1234", max_length=17)]
