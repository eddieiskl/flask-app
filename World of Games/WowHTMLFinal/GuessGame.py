# GuessGame.py
import random

class GuessGame:
    def __init__(self, player_name, difficulty):
        self.player_name = player_name
        self.difficulty = difficulty
        self.secret_number = random.randint(1, self.get_max_number())

    def get_max_number(self):
        # Adjust the maximum number based on difficulty
        return 2 ** self.difficulty

    def get_prompt(self):
        return f"Guess a number between 1 and {self.get_max_number()}:"

    def play(self, guess):
        try:
            guess = int(guess)
            return guess == self.secret_number
        except ValueError:
            raise ValueError("Invalid input. Please enter a valid number.")

    def get_correct_answer(self):
        return self.secret_number