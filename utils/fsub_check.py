from config import FSUB_CHANNEL_ID
from pyrogram.errors import UserNotParticipant, ChatAdminRequired

async def check_fsub(client, user_id: int) -> bool:
    try:
        member = await client.get_chat_member(FSUB_CHANNEL_ID, user_id)
        return member.status in ("member", "creator", "administrator")
    except UserNotParticipant:
        return False
    except ChatAdminRequired:
        # Bot is not admin in the channel
        return True
    except:
        return False
