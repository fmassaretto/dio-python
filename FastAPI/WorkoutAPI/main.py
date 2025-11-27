from fastapi import FastAPI
from routers import router
import uvicorn

app = FastAPI(title="WorkoutAPI")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", log_level="info", reload=True)