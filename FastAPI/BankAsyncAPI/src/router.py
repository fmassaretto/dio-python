from fastapi import APIRouter

from FastAPI.BankAsyncAPI.src.controllers import ClientController


router = APIRouter()

router.include_router(ClientController.router, prefix="/clients", tags=["clients"])
#router.include_router(CategoryController.router, prefix="/categories", tags=["categories"])
#router.include_router(TrainingCenterController.router, prefix="/training-center", tags=["training-center"])