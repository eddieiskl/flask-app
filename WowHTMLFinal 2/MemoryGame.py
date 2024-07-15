import random


class MemoryGame:
    def __init__(self, player_name, difficulty):
        self.player_name = player_name
        self.difficulty = difficulty
        self.sequence = self.generate_sequence()

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_prompt(self):
        return f"Remember this sequence: {self.sequence}"

    def play(self, guess):
        user_sequence = list(map(int, guess.split()))
        return self.sequence == user_sequence

    def get_correct_answer(self):
        return self.sequence