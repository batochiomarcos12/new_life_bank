from datetime import datetime
from typing import Dict
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def  root():
    return "Welcome to New Life Bank"

@app.get("/health")
def alive():
    return {"timestamp": datetime.now()}

if __name__ == "__main__":
    uvicorn.rum("main:app", host="0.0.0.0.", port=8004, reaload=True)    