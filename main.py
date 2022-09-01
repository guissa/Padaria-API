
 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_root():
    return {"Mensagem": "Hello World"}
