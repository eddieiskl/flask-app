# MemoryGame.py
import random

class MemoryGame:
    def __init__(self, player_name, difficulty):
        self.player_name = player_name
        self.difficulty = difficulty
        self.sequence = self.generate_sequence()

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_prompt(self):
        sequence_str = ' '.join(map(str, self.sequence))
        return f"Remember the following sequence: {sequence_str}"

    def play(self, guess):
        try:
            user_sequence = list(map(int, guess.split()))
            return user_sequence == self.sequence
        except ValueError:
            raise ValueError("Invalid input. Please enter a sequence of numbers separated by spaces.")

    def get_correct_answer(self):
        return ' '.join(map(str, self.sequence))