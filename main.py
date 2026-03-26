from fastapi import FastAPI
from pydantic import BaseModel

from services import analyze_text


class Item(BaseModel):
    text: str


class HealthResponse(BaseModel):
    status: str


class MessageResponse(BaseModel):
    message: str


class PredictionResponse(BaseModel):
    result: list[dict]


app = FastAPI(
    title="Sentiment Analysis API",
    description="API for text sentiment analysis using transformers.",
    version="1.0.0",
)


@app.get("/", response_model=MessageResponse)
def root() -> MessageResponse:
    return {"message": "FastAPI service started"}


@app.get("/health", response_model=HealthResponse)
def healthcheck() -> HealthResponse:
    return {"status": "ok"}


@app.post("/predict/", response_model=PredictionResponse)
def predict(item: Item) -> PredictionResponse:
    return {"result": analyze_text(item.text)}
