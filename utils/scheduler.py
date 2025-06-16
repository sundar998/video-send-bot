import asyncio

async def auto_delete_message(bot, chat_id, message_id, delay: int):
    await asyncio.sleep(delay)
    try:
        await bot.delete_messages(chat_id, message_id)
    except Exception as e:
        print(f"Auto-delete failed: {e}")
