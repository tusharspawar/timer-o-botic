from flask import Flask
from flask_restplus import Api
from config import config


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version='1.0',
            title='Timer-o-Botic',
            default="api",
            default_label="Timer Api's",
            doc='/docs',
        )
        self.app_start_time = None

    def run(self, env_name):
        self.app.config.from_object(config.get(env_name))
        self.app.run()


server = Server()
