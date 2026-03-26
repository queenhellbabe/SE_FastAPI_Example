from fastapi import FastAPI
from pydantic import BaseModel

from services import analyze_text


class Item(BaseModel):
    text: str


app = FastAPI(
    title="Sentiment Analysis API",
    description="API for text sentiment analysis using transformers.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "FastAPI service started"}


@app.get("/health")
def healthcheck():
    return {"status": "ok"}


@app.post("/predict/")
def predict(item: Item):
    return {"result": analyze_text(item.text)}
