import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/song")
def songList():

    with open('top_tracks_2023.json','r') as file:
        tracks = json.load(file)


    return jsonify(tracks)