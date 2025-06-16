from pyrogram import Client, filters
from config import OWNER_ID
from database.users import set_premium

def register_handlers(app: Client):
    @app.on_message(filters.command("addpremium") & filters.user(OWNER_ID))
    async def add_premium(client, message):
        if len(message.command) < 2:
            return await message.reply("Usage: /addpremium <user_id>")
        uid = int(message.command[1])
        set_premium(uid, True)
        await message.reply(f"✅ User {uid} is now premium.")

    @app.on_message(filters.command("removepremium") & filters.user(OWNER_ID))
    async def remove_premium(client, message):
        if len(message.command) < 2:
            return await message.reply("Usage: /removepremium <user_id>")
        uid = int(message.command[1])
        set_premium(uid, False)
        await message.reply(f"❌ User {uid} is no longer premium.")
