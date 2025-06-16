from pyrogram import Client, filters
from config import OWNER_ID
from database import db

def register_handlers(app: Client):
    @app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast_handler(client, message):
        if not message.reply_to_message:
            await message.reply("Reply to a message you want to broadcast.")
            return

        users = db.users.find()
        success, failed = 0, 0

        for user in users:
            try:
                await message.reply_to_message.copy(chat_id=user["user_id"])
                success += 1
            except:
                failed += 1

        await message.reply(f"✅ Broadcast completed.\nSuccess: {success}\nFailed: {failed}")
