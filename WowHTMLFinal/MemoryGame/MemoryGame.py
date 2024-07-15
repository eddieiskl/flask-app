from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/start/<int:difficulty>', methods=['GET'])
def start_game(difficulty):
    sequence = ''.join([str(random.randint(0, 9)) for _ in range(difficulty)])
    return jsonify({'sequence': sequence})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)