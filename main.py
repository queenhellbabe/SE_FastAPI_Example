from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

from services import analyze_text


class Item(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def text_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("text must not be blank or whitespace only")
        return v


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
    try:
        return {"result": analyze_text(item.text)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
