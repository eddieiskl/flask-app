from flask import Flask, render_template, request, redirect, url_for
from Live import welcome

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['POST'])
def welcome_user():
    player_name = request.form['player_name']
    welcome_message = welcome(player_name)
    return render_template('welcome.html', message=welcome_message, player_name=player_name)


@app.route('/select_game', methods=['GET', 'POST'])
def select_game():
    if request.method == 'POST':
        # Print detailed request information
        print("Form data:", request.form)  # Detailed debugging statement
        print("Request data:", request.data)  # Raw request data
        print("Request headers:", request.headers)  # Request headers
        print("Request environment:", request.environ)  # Environment variables

        player_name = request.form.get('player_name')
        game_choice = request.form.get('game_choice')
        difficulty = request.form.get('difficulty')

        if not game_choice:
            print("Debug - Form data missing game_choice field")  # Additional debug statement
            return "Missing game_choice", 400  # Return error response if game_choice is missing

        if game_choice == '1':
            return redirect(url_for('play_memory_game', player_name=player_name, difficulty=difficulty))
        elif game_choice == '2':
            return redirect(url_for('play_guess_game', player_name=player_name, difficulty=difficulty))
        elif game_choice == '3':
            return redirect(url_for('play_currency_roulette_game', player_name=player_name, difficulty=difficulty))

    player_name = request.args.get('player_name')
    return render_template('select_game.html', player_name=player_name)


@app.route('/play_memory_game')
def play_memory_game():
    player_name = request.args.get('player_name')
    difficulty = int(request.args.get('difficulty'))
    return redirect(f'http://localhost:5001/play?player_name={player_name}&difficulty={difficulty}')


@app.route('/play_guess_game')
def play_guess_game():
    player_name = request.args.get('player_name')
    difficulty = int(request.args.get('difficulty'))
    return redirect(f'http://localhost:5003/play?player_name={player_name}&difficulty={difficulty}')


@app.route('/play_currency_roulette_game')
def play_currency_roulette_game():
    player_name = request.args.get('player_name')
    difficulty = int(request.args.get('difficulty'))
    return redirect(f'http://localhost:5002/play?player_name={player_name}&difficulty={difficulty}')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)