from flask import Flask, request, jsonify
import random
import time

app = Flask(__name__)

@app.route('/start', methods=['POST'])
def start():
    difficulty = request.json['difficulty']
    sequence = [random.randint(1, 101) for _ in range(difficulty)]
    return jsonify({'sequence': sequence})

@app.route('/play', methods=['POST'])
def play():
    difficulty = request.json['difficulty']
    user_sequence = list(map(int, request.json['user_sequence']))
    sequence = [random.randint(1, 101) for _ in range(difficulty)]
    time.sleep(0.7)  # Simulate showing the sequence
    if user_sequence == sequence:
        result = "You won!"
    else:
        result = "You lost!"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)