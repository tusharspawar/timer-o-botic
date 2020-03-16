from server.instance import server

app = server.app


@app.errorhandler(404)
def path_not_found(error):
    return {"error": "path not found"}, 404


@app.errorhandler(500)
def server_error(error):
    print(error)
    return {"error": "server error"}, 500
