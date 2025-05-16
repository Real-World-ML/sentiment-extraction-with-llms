from baml_client.sync_client import b
from baml_client.types import CryptoSentiment

def get_sentiment(news: str) -> list[CryptoSentiment]: 
  
  # BAML's internal parser guarantees ExtractResume
  # to be always return a Resume type
  sentiment = b.ExtractCryptoSentiment(news)
  
  
  return sentiment