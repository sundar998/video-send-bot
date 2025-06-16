import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
OWNER_ID = int(os.getenv("OWNER_ID"))
FSUB_CHANNEL_ID = os.getenv("FSUB_CHANNEL_ID")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
