import os
from flask import Flask
import redis
app = Flask(__name__)

r = redis.Redis(host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT"), decode_responses=True)

@app.route("/count")
def getCount():
  return r.get('count')

@app.route("/")
def hello():
  r.incr('count')
  return "Hello World v3!"

app.run(host='0.0.0.0', port=os.environ.get("WEBSERVICE_PORT"), debug=True)