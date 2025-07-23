from flask import Flask
import os
import redis

app = Flask(__name__)
redis_host = os.environ.get('REDIS_HOST', 'redis-svc')
redis_password = os.environ.get('REDIS_PASSWORD')

r = redis.Redis(
    host=redis_host,
    port=6379,
    password=redis_password,
    decode_responses=True
)

@app.route('/')
def counter():
    count = r.incr('visitor_count')
    return f'Total Visitors: {count}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)