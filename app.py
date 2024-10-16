import json
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/song", methods=["POST", "OPTIONS"])
def songList():

    # Chat GPT. POST request simply would not be able to happen without this if statement
    # I kept getting 405 errors and CORS errors
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    # Opening the JSON file
    with open('top_tracks_2023.json') as file:
        tracks = json.load(file)


    # Getting the request
    data = request.get_json()

    # Getting all the search and sort forms
    search_field = data.get("searchField")
    sort_order = data.get("sortOrder")
    explicit = data.get("includeExp")
    search_box = data.get("searchBox").lower()

    #Creating an empty list
    filtered_songs = []

    # Iterating over each song
    # Chat GPT helped here
    for song in tracks:
        if search_field == "artists":

            # Check if search_box is in any of the artist names
            artists = [artist.lower() for artist in song['artists']]  # Lowercase all artist names

            if any(search_box in artist for artist in artists):
                # If the checkbox is checked, include explicit songs, otherwise filter them out
                if explicit or not song.get('explicit', False):
                    filtered_songs.append(song)

        # Check for genre search
        elif search_field == "genres":
            genres = [genre.lower() for genre in song['genres']]  # Lowercase all genre names
            if any(search_box in genre for genre in genres):
                if explicit or not song.get('explicit', False):
                    filtered_songs.append(song)

        # Check title
        else:
            if search_box in song[search_field].lower():
                # If the checkbox is checked, include explicit songs, otherwise filter them out
                if explicit or not song.get('explicit', False):
                    filtered_songs.append(song)

    # Sort the filtered songs based on the selected sort order
    if sort_order == "popularity":
        # Chat GPT helped here, showed me a quick and efficient way to sort in Python
        # This is similar to Java how we can say something is of type T
        filtered_songs.sort(key=lambda x: x['popularity'], reverse=True)
    elif sort_order == "duration":
        filtered_songs.sort(key=lambda x: x['duration_mins'])

    return jsonify(filtered_songs)

