# MemoryGame.py

import random
import time
from Utils import screen_cleaner

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = []

    def generate_sequence(self):
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        user_sequence = []
        print("Please enter the numbers you remember, one at a time:")
        for _ in range(self.difficulty):
            while True:
                try:
                    number = int(input())
                    user_sequence.append(number)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        return user_sequence

    def is_list_equal(self, user_sequence):
        return user_sequence == self.sequence

    def play(self):
        self.generate_sequence()
        print(f"Remember this sequence: {self.sequence}")
        time.sleep(0.7)
        screen_cleaner()
        user_sequence = self.get_list_from_user()
        if self.is_list_equal(user_sequence):
            print("You won!")
        else:
            print("You lost!")

if __name__ == "__main__":
    difficulty = int(input("Enter difficulty: "))
    game = MemoryGame(difficulty)
    game.play()