import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SLACK_TOKEN = os.getenv("SLACK_TOKEN")
    SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")
