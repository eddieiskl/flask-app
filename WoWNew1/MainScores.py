# MainScores.py

from flask import Flask, render_template_string
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read()
            return render_template_string("""
                <html>
                <head>
                <title>Scores Game</title>
                </head>
                <body>
                <h1>The score is <div id="score">{{ score }}</div></h1>
                </body>
                </html>
            """, score=score)
    except Exception as e:
        return render_template_string("""
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <h1><div id="score" style="color:red">{{ error }}</div></h1>
            </body>
            </html>
        """, error=str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)