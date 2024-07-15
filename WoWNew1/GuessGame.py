# GuessGame.py

import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                guess = int(input(f"Enter your guess (1 to {self.difficulty}): "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print(f"Please enter a number between 1 and {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def compare_results(self, guess):
        return guess == self.secret_number

    def play(self):
        self.generate_number()
        guess = self.get_guess_from_user()
        if self.compare_results(guess):
            print("You won!")
        else:
            print("You lost!")

if __name__ == "__main__":
    difficulty = int(input("Enter difficulty: "))
    game = GuessGame(difficulty)
    game.play()