from flask import Flask, render_template, request, redirect, url_for, abort
import redis
import re
from functools import wraps
import time
import os

app = Flask(__name__)

# Rate limiting settings
RATE_LIMIT = 5  # max requests
RATE_PERIOD = 60  # seconds

def get_redis():
    return redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def rate_limiter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        r = get_redis()
        ip = request.remote_addr
        key = f"rate_limit:{ip}"
        current = r.get(key)
        if current and int(current) >= RATE_LIMIT:
            abort(429, description="Too Many Requests")
        else:
            pipe = r.pipeline()
            pipe.incr(key, 1)
            pipe.expire(key, RATE_PERIOD)
            pipe.execute()
        return func(*args, **kwargs)
    return wrapper

@app.before_request
def enforce_https():
    if not request.is_secure and os.environ.get("FLASK_ENV") == "production":
        url = request.url.replace("http://", "https://", 1)
        return redirect(url, code=301)

@app.route('/', methods=['GET'])
def main_page():
    return render_template('collect_email.html')

@app.route('/submit_email', methods=['POST'])
@rate_limiter
def submit_email():
    email = request.form['email']
    if email and is_valid_email(email):
        r = get_redis()
        r.sadd('emails', email)
        return redirect(url_for('thank_you'))
    return redirect(url_for('main_page'))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)