from flask import jsonify
from server.instance import server

app = server.app


@app.after_request
def after_request(response):
    return jsonify(response)
