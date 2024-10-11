from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/song")
def songList():

    file = open('top_tracks_2024.json','r')


    return jsonify(file)