from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH
from handlers import start, video_delivery, broadcast, premium, referral, verify_token

# Initialize Pyrogram client
app = Client(
    "post_send_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Register handlers
start.register_handlers(app)
video_delivery.register_handlers(app)
broadcast.register_handlers(app)
premium.register_handlers(app)
referral.register_handlers(app)
verify_token.register_handlers(app)

# Run the bot
app.run()
