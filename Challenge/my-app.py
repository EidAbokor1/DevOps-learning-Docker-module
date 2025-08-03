from flask import Flask, render_template, redirect, url_for
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/count')
def count():
    visits = r.incr("counter")
    return render_template("count.html", visits=visits)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
