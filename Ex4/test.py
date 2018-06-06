from flask import Flask, request
from redis import Redis
redis = Redis(host='127.0.0.1', port=6379)
app = Flask(__name__)

@app.route("/")
def main():
    user_agent = request.headers.get('User-Agent')
    redis.pfadd('user', user_agent)
    count_ua = redis.pfcount('user')
    print user_agent
    return '<p>Your browser is {}!</p><p>Count user-agent: {} browser</p>'.format(user_agent, count_ua)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug = True)