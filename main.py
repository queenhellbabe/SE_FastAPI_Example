import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

from logging_config import configure_logging
from services import analyze_text

configure_logging()
logger = logging.getLogger(__name__)


class Item(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def text_must_not_be_blank(cls, v: str) -> str:
        stripped = v.strip()
        if not stripped:
            raise ValueError("text must not be blank or whitespace only")
        if len(stripped) > 512:
            raise ValueError("text must not exceed 512 characters")
        return stripped


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
    logger.info("Received predict request, text length: %d", len(item.text))
    try:
        result = analyze_text(item.text)
        logger.info("Prediction successful: label=%s score=%.4f", result[0]["label"], result[0]["score"])
        return {"result": result}
    except ValueError as e:
        logger.warning("Validation error: %s", e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        logger.exception("Unexpected error during prediction")
        raise HTTPException(status_code=500, detail="Internal server error")
