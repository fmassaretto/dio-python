from fastapi import FastAPI
import uvicorn

from FastAPI.BankAsyncAPI.src import router


app = FastAPI(title="BankAPI")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", log_level="info", reload=True)