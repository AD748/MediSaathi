import redis
import json

redis_client = redis.Redis(
    host="localhost",
    port=6380,
    decode_responses=True
)

SESSION_TTL = 3600


def save_session(session_id, data):

    redis_client.setex(
        session_id,
        SESSION_TTL,
        json.dumps(data)
    )


def get_session(session_id):

    data = redis_client.get(session_id)

    if data:
        return json.loads(data)

    return {}