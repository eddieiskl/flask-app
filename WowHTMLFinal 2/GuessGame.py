import random


class GuessGame:
    def __init__(self, player_name, difficulty):
        self.player_name = player_name
        self.difficulty = difficulty
        self.secret_number = random.randint(1, difficulty * 10)

    def get_prompt(self):
        return f"Guess the number between 1 and {self.difficulty * 10}:"

    def play(self, guess):
        guess = int(guess)
        return guess == self.secret_number

    def get_correct_answer(self):
        return self.secret_number