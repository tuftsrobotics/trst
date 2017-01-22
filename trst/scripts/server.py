"""
Implements a server on port 8888 with simple json posting
API:
    '/' all data unioned
    '/waypoints' waypoint data
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

class Server(object):
    data = {}
    waypoints = {}

    @app.route('/', methods = ['GET', 'POST'])
    def index_post():
        if request.method == 'POST':
            server.data.update(request.json)
        return jsonify(server.data)

    @app.route('/waypoint', methods = ['GET', 'POST'])
    def waypoint_method():
        if request.method == 'POST':
            server.waypoints.update(request.json)
        return jsonify(server.waypoints)

server = Server()

def run():
    app.run(host = '0.0.0.0', port = 8888)

if __name__ == "__main__":
    run()
