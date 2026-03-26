from functools import lru_cache

from transformers import pipeline


@lru_cache
def get_classifier():
    return pipeline("sentiment-analysis")


def analyze_text(text: str):
    classifier = get_classifier()
    return classifier(text)
