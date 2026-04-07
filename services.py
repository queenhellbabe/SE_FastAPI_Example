import logging
import time
from functools import lru_cache

from transformers import pipeline

logger = logging.getLogger(__name__)


@lru_cache
def get_classifier():
    logger.info("Loading sentiment-analysis model")
    return pipeline("sentiment-analysis")


def analyze_text(text: str):
    classifier = get_classifier()
    start = time.perf_counter()
    result = classifier(text.strip())
    elapsed = time.perf_counter() - start
    logger.info("Inference completed in %.3fs", elapsed)
    return result
