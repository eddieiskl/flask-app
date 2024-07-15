import requests
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
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
    if request.method == "POST":
        player_name = request.form.get("player_name")
        if player_name:
            return redirect(url_for("main_menu", player_name=player_name))
    return render_template("index.html", welcome_gif=welcome_gif)

@app.route("/main_menu", methods=["GET", "POST"])
def main_menu():
    player_name = request.args.get("player_name")
    if request.method == "POST":
        game_choice = request.form.get("game_choice")
        if game_choice == "MemoryGame":
            return redirect(url_for("start_memory_game", player_name=player_name))
        elif game_choice == "GuessGame":
            return redirect(url_for("start_guess_game", player_name=player_name))
        elif game_choice == "CurrencyRouletteGame":
            return redirect(url_for("start_currency_roulette_game", player_name=player_name))
    return render_template("main_menu.html", player_name=player_name)

@app.route("/win")
def win():
    return render_template("win.html")

@app.route("/lose")
def lose():
    return render_template("lose.html")

@app.route("/start_memory_game")
def start_memory_game():
    player_name = request.args.get("player_name")
    return redirect(f"http://localhost:5001?player_name={player_name}")

@app.route("/start_guess_game")
def start_guess_game():
    player_name = request.args.get("player_name")
    return redirect(f"http://localhost:5002?player_name={player_name}")

@app.route("/start_currency_roulette_game")
def start_currency_roulette_game():
    player_name = request.args.get("player_name")
    return redirect(f"http://localhost:5003?player_name={player_name}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)