from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    player_name = request.form['player_name']
    return render_template('menu.html', player_name=player_name)


@app.route('/memory')
def memory():
    return render_template('memory.html')


@app.route('/play_memory', methods=['POST'])
def play_memory():
    difficulty = int(request.form['difficulty'])
    response = requests.post(f'http://memory_game:5001/start', json={'difficulty': difficulty})

    sequence = response.json().get('sequence', [])

    return render_template('memory_play.html', difficulty=difficulty, sequence=sequence)


@app.route('/submit_memory', methods=['POST'])
def submit_memory():
    difficulty = int(request.form['difficulty'])
    user_sequence = request.form['user_sequence'].split()
    response = requests.post(f'http://memory_game:5001/play',
                             json={'difficulty': difficulty, 'user_sequence': user_sequence})

    result = response.json().get('result', 'Error')
    return render_template('memory_result.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)