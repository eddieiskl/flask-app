import random
import requests

class CurrencyRouletteGame:
    def __init__(self, player_name, difficulty):
        self.player_name = player_name
        self.difficulty = difficulty
        self.amount = random.randint(1, 100)
        self.rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return data["rates"]["ILS"]

    def get_prompt(self):
        return f"Guess the value of {self.amount} USD in ILS (within {self.difficulty} ILS):"

    def play(self, guess):
        guess = float(guess)
        correct_value = self.amount * self.rate
        return abs(correct_value - guess) <= self.difficulty

    def get_correct_answer(self):
        return self.amount * self.rate