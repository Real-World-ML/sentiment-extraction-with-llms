# A FastAPI server with one GET endpoint called sentiment where the user
# can pass in a string and get back a sentiment score between -1 and 1.

from fastapi import FastAPI
from baml_client.sync_client import b
from baml_client.types import CryptoSentiment
from loguru import logger
from typing import Any
from sentiment import get_sentiment

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/sentiment")
async def sentiment(text: str) -> dict[str, Any]:
    
    logger.info(f'Received sentiment request: {text}')

    # Use BAML to analyze the sentiment
    # sentiments = b.ExtractCryptoSentiment(text)
    sentiments = get_sentiment(text)

    # Convert BAML sentiment to a numeric score
    # Positive = 1, Neutral = 0, Negative = -1
    score_map = {
        "Positive": 1.0,
        "Neutral": 0.0,
        "Negative": -1.0
    }
    # breakpoint()

    response = {'sentiment': [{'coin': sentiment.coin, 'score': score_map[sentiment.score]} for sentiment in sentiments]}

    return response