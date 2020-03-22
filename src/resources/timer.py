import time
import datetime
from dateutil.tz import tzlocal
from flask import g, jsonify, after_this_request
from flask_restplus import Resource
from server.instance import server
from util.execution_time import execution_time

api = server.api


@api.route('/api/uptime')
class Timer(Resource):
    @execution_time
    def get(self):
        current_datetime = {
            "currentDateTime": datetime.datetime.now(tzlocal()).strftime('%Y-%m-%d %H:%M:%S %Z')
        }

        @after_this_request
        def add_response_time(response):
            response_data = response.get_json()
            response_data["responseTimeMs"] = "{:.4f}".format((time.time() - g.request_start_time) * 1000)
            response_data["appUptimeSec"] = round((time.time() - g.app_start_time))
            return jsonify(response_data)

        return current_datetime
