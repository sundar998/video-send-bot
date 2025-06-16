from database import db

referrals = db.referrals

def add_referral(inviter_id: int, invited_id: int):
    existing = referrals.find_one({"inviter_id": inviter_id})
    if existing:
        if invited_id not in existing.get("invited_ids", []):
            referrals.update_one(
                {"inviter_id": inviter_id},
                {"$push": {"invited_ids": invited_id}}
            )
    else:
        referrals.insert_one({
            "inviter_id": inviter_id,
            "invited_ids": [invited_id]
        })

def get_referral_count(inviter_id: int):
    data = referrals.find_one({"inviter_id": inviter_id})
    return len(data.get("invited_ids", [])) if data else 0
