from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/roulette', methods=['POST'])
def roulette():
    data = request.get_json()
    difficulty = data['difficulty']
    correct_answer = round(random.uniform(1, 10) * difficulty, 2)
    return jsonify({'correct_answer': correct_answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)