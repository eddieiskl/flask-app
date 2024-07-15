# GuessGame.py
import random

class GuessGame:
    def __init__(self, player_name, difficulty):
        # Initialize the game with the player's name and the chosen difficulty level
        self.player_name = player_name
        self.difficulty = difficulty
        # Generate the secret number based on the difficulty level
        self.secret_number = self.generate_number()

    # Generate a random number between 1 and the difficulty level
    def generate_number(self):
        return random.randint(1, self.difficulty)

    # Prompt the player to guess the number
    def get_guess_from_user(self):
        guess = input(f"{self.player_name}, please guess a number between 1 and {self.difficulty}: ")
        # Validate the input to ensure it is a number within the correct range
        while not guess.isdigit() or not (1 <= int(guess) <= self.difficulty):
            guess = input(f"Invalid input. Please enter a number between 1 and {self.difficulty}: ")
        return int(guess)

    # Compare the player's guess with the secret number
    def compare_results(self, guess):
        return guess == self.secret_number

    # Play the Guess Game
    def play(self):
        # Get the player's guess
        guess = self.get_guess_from_user()
        # Check if the guess matches the secret number
        if self.compare_results(guess):
            # If the guess is correct, return True
            return True
        else:
            # If the guess is incorrect, inform the player of the correct number and return False
            print(f"Sorry, {self.player_name}. The correct number was {self.secret_number}.")
            return False