from fastapi import APIRouter
from controllers import TrainingCenterController
from controllers import CategoryController
from controllers import AthleteController

router = APIRouter()

router.include_router(AthleteController.router, prefix="/athletes", tags=["athletes"])
router.include_router(CategoryController.router, prefix="/categories", tags=["categories"])
router.include_router(TrainingCenterController.router, prefix="/training-center", tags=["training-center"])