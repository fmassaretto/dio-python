import uuid
from FastAPI.BankAsyncAPI.src.configs.dependencies import DatabaseDependency
from FastAPI.BankAsyncAPI.src.models.ClientEntity import ClientEntity
from FastAPI.BankAsyncAPI.src.schemas.requests.ClientRequest import ClientRequest
from FastAPI.BankAsyncAPI.src.schemas.responses import ClientResponse


class ClientRepository():
    db_session = DatabaseDependency

    async def save(self, client_request: ClientRequest) -> ClientResponse:
        client_response = ClientResponse(id=uuid(), **client_request.model_dump())

        client_db_model = ClientEntity(**client_response.model_dump())

        self.db_session.add(client_db_model)

        await self.db_session.commit()

        return client_response