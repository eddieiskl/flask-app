from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    difficulty = data['difficulty']
    guess = data['guess']
    # Your game logic here...
    return jsonify(result="Currency Roulette Game played successfully")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)