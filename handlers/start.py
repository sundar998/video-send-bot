from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID, FSUB_CHANNEL_ID
from utils.fsub_check import check_fsub
from database.users import get_user

def register_handlers(app: Client):
    @app.on_message(filters.command("start"))
    async def start_handler(client, message):
        user_id = message.from_user.id

        # Force Subscribe Check
        if not await check_fsub(client, user_id):
            btn = InlineKeyboardMarkup([[
                InlineKeyboardButton("🔔 Join Channel", url=f"https://t.me/{FSUB_CHANNEL_ID.replace('@', '')}")
            ]])
            await message.reply("🚫 You must join the updates channel first!", reply_markup=btn)
            return

        # Add user to DB
        get_user(user_id)

        # Token referral handler
        if len(message.command) > 1:
            payload = message.command[1]
            if payload.startswith("verify"):
                from handlers.verify_token import process_token
                await process_token(client, message, payload)
                return
            elif payload.startswith("ref"):
                from handlers.referral import handle_referral
                await handle_referral(user_id, payload[3:])

        await message.reply("✅ You're ready!\nClick 'Get Start' to begin receiving videos.")

