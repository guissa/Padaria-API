import os
from typing import Optional
from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/")
def hello_root():
    return {"Mensagem": "Eu sou o gui"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
