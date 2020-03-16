import time
from flask import g
from server.instance import server

app = server.app


@app.before_first_request
def before_first_request():
    server.app_start_time = time.time()


@app.before_request
def before_request():
    g.app_start_time = server.app_start_time
    g.request_start_time = time.time()
