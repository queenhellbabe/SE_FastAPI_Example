from functools import lru_cache

from transformers import pipeline


@lru_cache
def get_classifier():
    return pipeline("sentiment-analysis")


def analyze_text(text: str):
    normalized_text = text.strip()
    if not normalized_text:
        raise ValueError("Text for analysis must not be empty.")

    classifier = get_classifier()
    return classifier(normalized_text)
