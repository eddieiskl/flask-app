from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu', methods=['POST'])
def menu():
    player_name = request.form['player_name']
    if player_name.lower() == 'q':
        return redirect(url_for('quit'))
    return render_template('menu.html', player_name=player_name)

@app.route('/memory_game/<int:difficulty>', methods=['GET', 'POST'])
def memory_game(difficulty):
    if request.method == 'POST':
        # Generate a sequence of numbers based on the difficulty level
        sequence = generate_sequence(difficulty)
        return render_template('game.html', sequence=sequence)
    return redirect(url_for('menu'))

def generate_sequence(difficulty):
    # Placeholder function to generate a sequence of numbers
    # The actual implementation can vary based on your game logic
    import random
    return ''.join([str(random.randint(0, 9)) for _ in range(difficulty)])

@app.route('/result', methods=['POST'])
def result():
    user_input = request.form.get('user_input')
    correct_sequence = request.form.get('sequence')
    if user_input == correct_sequence:
        result_message = "Correct!"
        result_gif = url_for('static', filename='images/success.gif')
    else:
        result_message = "Incorrect!"
        result_gif = url_for('static', filename='images/failure.gif')
    return render_template('result.html', result_message=result_message, result_gif=result_gif, correct_sequence=correct_sequence)

@app.route('/quit')
def quit():
    return render_template('goodbye.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')