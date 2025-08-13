from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestData(BaseModel):
    ticketId: str

@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running!"}

@app.post("/analyze")
def analyze_ticket(data: RequestData):
    return {
        "ticketId": data.ticketId,
        "analysis": "This is a dummy AI-based analysis result."
    }
