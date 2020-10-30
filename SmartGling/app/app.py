from flask import Flask, request, Response
import redis
import time
import random

app = Flask(__name__)

pool = redis.ConnectionPool(host='redis', port=6379, db=0)

def gen(n):
    strings = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789a"
    return "".join(random.choice(strings) for _ in range(n))

def init():
    try:
        r = redis.Redis(connection_pool=pool)
        r.set("SuperGate_1s_s0_SuperGay_nonfioasacmamwd", 'admin')
    except Exception as e:
        print(e)
        return 'error'

def check_admin(k):
    try:
        r = redis.Redis(connection_pool=pool)
        v = r.get(k)
        print(v)
        if v == b'admin':
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

@app.route("/", methods = ['GET', 'POST'])
def index():
    try:
        key = request.headers.get('ROLE')
        if key == None:
            r = redis.Redis(connection_pool=pool)
            _k = gen(9)+str(int(time.time()))
            r.set(_k, "guest")
            return Response("hello!"+"<br>", headers = {"ROLE":_k})
    except Exception as e:
        print(e)
        return 'error'

    return "hello!"+"<br>"

@app.route("/getflag", methods = ['GET', 'POST'])
def getflag():
    try:
        key = request.headers.get('ROLE')
        if check_admin(key):
            return Response(open('/flag', 'r').read(), mimetype='text/plain')
        else:
            return "You are not Admin!"+"<br>"
    except Exception as e:
        print(e)
        return 'error'

@app.route("/upgrade_role", methods = ['GET', 'POST'])
def changerole():
    try:
        key = request.headers.get('ROLE')
        if check_admin(key):
            r = redis.Redis(connection_pool=pool)
            r.set(request.args.get('role'), 'admin')
            return "Ok!"+"<br>"
        else:
            return "You are not Admin!"+"<br>"
    except Exception as e:
        print(e)
        return 'error'

@app.route("/source", methods = ['GET', 'POST'])
def source():
    return Response(open('/app/source', 'r').read(), mimetype='text/plain')

if __name__ == '__main__':
    init()
    app.run(host='0.0.0.0', port=9527)
