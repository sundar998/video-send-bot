from database import db
from datetime import datetime

users = db.users

def get_user(user_id):
    user = users.find_one({"user_id": user_id})
    if not user:
        users.insert_one({
            "user_id": user_id,
            "daily_count": 0,
            "last_reset": datetime.utcnow(),
            "is_premium": False,
            "referrals": [],
            "last_video_id": None
        })
        return get_user(user_id)
    return user

def increment_video_count(user_id):
    user = get_user(user_id)
    now = datetime.utcnow()
    last_reset = user.get("last_reset")

    # Reset if 24 hours passed
    if (now - last_reset).total_seconds() >= 86400:
        users.update_one({"user_id": user_id}, {
            "$set": {"daily_count": 1, "last_reset": now}
        })
    else:
        users.update_one({"user_id": user_id}, {
            "$inc": {"daily_count": 1}
        })

def set_premium(user_id, value=True):
    users.update_one({"user_id": user_id}, {"$set": {"is_premium": value}})

def is_premium(user_id):
    user = get_user(user_id)
    return user.get("is_premium", False)

def get_daily_count(user_id):
    user = get_user(user_id)
    return user.get("daily_count", 0)
