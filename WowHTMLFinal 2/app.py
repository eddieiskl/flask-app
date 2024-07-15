import requests
from flask import Flask, render_template, request, redirect, url_for
from Live import welcome, load_game
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame

app = Flask(__name__)

player_name = ""
last_game = None
last_difficulty = None
game_instance = None

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


def initialize_game():
    global game_instance
    if last_game == 1:
        game_instance = MemoryGame(player_name, last_difficulty)
    elif last_game == 2:
        game_instance = GuessGame(player_name, last_difficulty)
    elif last_game == 3:
        game_instance = CurrencyRouletteGame(player_name, last_difficulty)


def get_scores():
    try:
        with open("Scores.txt", 'r') as score_file:
            scores = eval(score_file.read().strip())
    except (FileNotFoundError, ValueError):
        scores = {"MemoryGame": 0, "GuessGame": 0, "CurrencyRouletteGame": 0}
    return scores


@app.route("/", methods=["GET", "POST"])
def index():
    global player_name
    welcome_gif = get_gif('welcome')
    if request.method == "POST":
        player_name = request.form.get("player_name")
        if player_name.lower() == 'q':
            return redirect(url_for("quit"))
        return redirect(url_for("menu"))
    return render_template("index.html", welcome_gif=welcome_gif)


@app.route("/menu", methods=["GET", "POST"])
def menu():
    global last_game, last_difficulty
    scores = get_scores()
    if request.method == "POST":
        game_choice = request.form.get("game_choice")
        if game_choice == 'q':
            return redirect(url_for("quit"))
        difficulty = request.form.get("difficulty")
        if difficulty == 'q':
            return redirect(url_for("quit"))
        if game_choice and difficulty and game_choice.isdigit() and difficulty.isdigit():
            last_game = int(game_choice)
            last_difficulty = int(difficulty)
            initialize_game()
            return redirect(url_for("play_game"))
    return render_template("menu.html", welcome_message=welcome(player_name), scores=scores)


@app.route("/play", methods=["GET", "POST"])
def play_game():
    global game_instance
    error_message = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input is None:
            error_message = "No input received. Please enter your guess."
            return render_template("game.html", game_prompt=game_instance.get_prompt(), error_message=error_message)
        if user_input == 'q':
            return redirect(url_for("quit"))
        try:
            if game_instance.play(user_input):
                victory_gif = get_gif('victory')
                return render_template("result.html", result="won", correct_answer=game_instance.get_correct_answer(),
                                       result_gif=victory_gif)
            else:
                losing_gif = get_gif('fail')
                return render_template("result.html", result="lost", correct_answer=game_instance.get_correct_answer(),
                                       result_gif=losing_gif)
        except ValueError as e:
            error_message = str(e)
    return render_template("game.html", game_prompt=game_instance.get_prompt(), error_message=error_message)


@app.route("/result", methods=["GET", "POST"])
def result():
    global last_game, last_difficulty
    if request.method == "POST":
        choice = request.form.get("choice")
        if choice == 'q':
            return redirect(url_for("quit"))
        elif choice == 'm':
            return redirect(url_for("menu"))
        elif choice == 'r':
            initialize_game()  # Reinitialize the game for retry
            return redirect(url_for("play_game"))
        elif choice == 's':
            return redirect(url_for("score_server"))
    return render_template("result.html")


@app.route("/quit", methods=["GET", "POST"])
def quit():
    quit_gif = get_gif('goodbye')
    if request.method == "POST":
        choice = request.form.get("choice")
        if choice == 'confirm':
            return render_template("goodbye.html", quit_gif=quit_gif)
        elif choice == 'cancel':
            return redirect(url_for("menu"))
    return render_template("quit.html", quit_gif=quit_gif)


@app.route("/score", methods=['GET'])
def score_server():
    try:
        # Read the current scores from the file
        with open("Scores.txt", 'r') as score_file:
            scores = eval(score_file.read().strip())
        return f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>High Scores</h1>
                <p>Memory Game: {scores["MemoryGame"]}</p>
                <p>Guess Game: {scores["GuessGame"]}</p>
                <p>Currency Roulette: {scores["CurrencyRouletteGame"]}</p>
            </body>
        </html>
        """
    except Exception as e:
        # Return an error message in an HTML template if something goes wrong
        return f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">Error: {e}</div></h1>
            </body>
        </html>
        """


if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000, debug=True)