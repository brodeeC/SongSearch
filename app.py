import json
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/song", methods=["POST", "OPTIONS"])
def songList():

    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    with open('top_tracks_2023.json') as file:
        tracks = json.load(file)

    return jsonify(tracks)

