from fastapi import FastAPI
import uvicorn
from logic.addition import add2
from logic.multiply import multiply2
from model.jsonConverter import convJSON

app = FastAPI()

@app.get("/")
def home():
    return convJSON("Hi!")

@app.get("/health")
def health():
    return convJSON("OK")

@app.get("/add")
def addition():
    return convJSON(add2())


@app.get("/multiply")
def multiply():
    return convJSON(multiply2())

if __name__ == "__main__":
    uvicorn.run(app)