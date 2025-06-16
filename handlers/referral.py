from pyrogram import Client, filters
from config import OWNER_ID
from database import db
from database.users import get_user, set_premium

ref_collection = db.referrals

def register_handlers(app: Client):
    @app.on_message(filters.command("myref"))
    async def my_ref(client, message):
        uid = message.from_user.id
        link = f"https://t.me/{(await client.get_me()).username}?start=ref{uid}"
        data = ref_collection.find_one({"inviter_id": uid}) or {}
        count = len(data.get("invited_ids", []))
        await message.reply(f"👥 Your referral link:\n{link}\n\nTotal invited: {count}")

    @app.on_message(filters.command("refstats") & filters.user(OWNER_ID))
    async def ref_stats(client, message):
        if len(message.command) < 2:
            return await message.reply("Usage: /refstats <user_id>")
        uid = int(message.command[1])
        data = ref_collection.find_one({"inviter_id": uid}) or {}
        count = len(data.get("invited_ids", []))
        await message.reply(f"User {uid} invited {count} users.")

async def handle_referral(user_id, inviter_id):
    inviter_id = int(inviter_id)
    if user_id == inviter_id:
        return
    existing = ref_collection.find_one({"inviter_id": inviter_id})
    if existing:
        if user_id in existing.get("invited_ids", []):
            return
        existing["invited_ids"].append(user_id)
        ref_collection.update_one({"inviter_id": inviter_id}, {"$set": {"invited_ids": existing["invited_ids"]}})
    else:
        ref_collection.insert_one({"inviter_id": inviter_id, "invited_ids": [user_id]})
    set_premium(inviter_id, True)
