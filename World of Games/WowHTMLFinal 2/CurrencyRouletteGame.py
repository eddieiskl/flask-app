# CurrencyRouletteGame.py
import random

class CurrencyRouletteGame:
    def __init__(self, player_name, difficulty):
        self.player_name = player_name
        self.difficulty = difficulty
        self.amount = random.randint(1, 100)  # Amount in USD
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        # Mock exchange rate; replace with actual API call if needed
        return 3.5

    def get_prompt(self):
        return f"Try to guess the value of {self.amount} USD in ILS."

    def play(self, guess):
        try:
            guess = float(guess)
            lower_bound = self.amount * self.exchange_rate * (1 - 0.1 / self.difficulty)
            upper_bound = self.amount * self.exchange_rate * (1 + 0.1 / self.difficulty)
            return lower_bound <= guess <= upper_bound
        except ValueError:
            raise ValueError("Invalid input. Please enter a valid number.")

    def get_correct_answer(self):
        return round(self.amount * self.exchange_rate, 2)