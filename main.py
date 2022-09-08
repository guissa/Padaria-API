import os
from typing import Optional
from fastapi import FastAPI
import uvicorn
from random import randint

app = FastAPI()

@app.get("/soma")
async def sum(n1: int = 15, n2: int = 15):
    return n1 + n2

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
