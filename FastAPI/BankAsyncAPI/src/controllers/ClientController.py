from fastapi import APIRouter, Body, status

from FastAPI.BankAsyncAPI.src.schemas.requests.ClientRequest import ClientRequest
from FastAPI.BankAsyncAPI.src.schemas.responses.ClientResponse import ClientResponse
from FastAPI.BankAsyncAPI.src.services.ClientService import ClientService


router = APIRouter()
service = ClientService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClientResponse)
def create_client(client_request: ClientRequest = Body(...)):
    return service.save(client_request)