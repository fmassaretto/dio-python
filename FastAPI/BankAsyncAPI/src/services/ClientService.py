from FastAPI.BankAsyncAPI.src.repositories.ClientRepository import ClientRepository
from FastAPI.BankAsyncAPI.src.schemas.requests.ClientRequest import ClientRequest


class ClientService():
    repo = ClientRepository()

    def save(self, client_request: ClientRequest):
        return self.repo.save(client_request)