from database.users import get_user

valid_tokens = {
    "verifyTOKEN123": 3,  # token: number of extra videos
    "verifyTOKEN456": 5
}

async def process_token(client, message, token):
    uid = message.from_user.id
    user = get_user(uid)
    token_str = token.strip()

    if token_str in valid_tokens:
        extra = valid_tokens[token_str]
        # Add extra daily limit to user (you can store in DB if needed)
        message.reply_text(f"✅ Token accepted! You've unlocked {extra} extra videos today.")
    else:
        await message.reply("❌ Invalid token.")
