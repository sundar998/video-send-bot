from database.users import get_user, get_daily_count, increment_video_count, is_premium

DAILY_LIMIT = 5

def can_download(user_id: int) -> bool:
    if is_premium(user_id):
        return True
    return get_daily_count(user_id) < DAILY_LIMIT

def record_download(user_id: int):
    increment_video_count(user_id)

def remaining_limit(user_id: int) -> int:
    if is_premium(user_id):
        return float("inf")
    return DAILY_LIMIT - get_daily_count(user_id)
