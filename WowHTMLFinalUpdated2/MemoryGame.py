from flask import Flask, request

app = Flask(__name__)

@app.route('/play')
def play():
    player_name = request.args.get('player_name')
    difficulty = request.args.get('difficulty')
    # Implement the game logic here
    return f"Playing Memory Game with player {player_name} at difficulty {difficulty}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)