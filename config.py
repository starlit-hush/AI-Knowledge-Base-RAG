import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
ENDPOINT_ID = os.getenv("ENDPOINT_ID")
EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"