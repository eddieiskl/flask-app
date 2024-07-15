# MemoryGame/app.py

import requests
from flask import Flask, request, render_template, send_from_directory
from MemoryGame import MemoryGame
import os

app = Flask(__name__)

GIPHY_API_KEY = "tb2FOxW74MH5X43Yn3gSpDGjLN4xiYd2"

def get_gif(tag):
    url = f"https://api.giphy.com/v1/gifs/random?api_key={GIPHY_API_KEY}&tag={tag}&rating=g"
    response = requests.get(url)
    data = response.json()

    try:
        gif_url = data['data']['images']['downsized_large']['url']
    except (KeyError, TypeError, IndexError) as e:
        print(f"Error fetching gif: {e}")
        gif_url = None

    return gif_url

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/", methods=["GET", "POST"])
def index():
    welcome_gif = get_gif('welcome')
    return render_template("index.html", welcome_gif=welcome_gif)

@app.route("/play", methods=["GET", "POST"])
def play_game():
    error_message = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            try:
                game_instance = MemoryGame("Player", 1)
                if game_instance.play(user_input):
                    victory_gif = get_gif('victory')
                    return render_template("result.html", result="won", correct_answer=game_instance.get_correct_answer(), result_gif=victory_gif)
                else:
                    losing_gif = get_gif('fail')
                    return render_template("result.html", result="lost", correct_answer=game_instance.get_correct_answer(), result_gif=losing_gif)
            except ValueError as e:
                error_message = str(e)
    return render_template("game.html", error_message=error_message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)