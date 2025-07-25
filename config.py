import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MONGO_URI = os.environ.get("MONGO_URI")
OWNER_ID = int(os.environ.get("OWNER_ID"))
FSUB_CHANNEL_ID = os.environ.get("FSUB_CHANNEL_ID")
VIDEO_DELETE_TIMER = int(os.environ.get("VIDEO_DELETE_TIMER", 60))  # Default 60s if not set
