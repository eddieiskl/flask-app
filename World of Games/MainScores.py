# MainScores.py

from flask import Flask
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)

@app.route('/score', methods=['GET'])
def score_server():
    try:
        # Read the current scores from the file
        with open(SCORES_FILE_NAME, 'r') as score_file:
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
                <h1><div id="score" style="color:red">{BAD_RETURN_CODE}</div></h1>
            </body>
        </html>
        """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)