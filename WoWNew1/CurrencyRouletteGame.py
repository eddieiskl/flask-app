# CurrencyRouletteGame.py

import random
import requests

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        # Replace 'your_api_key' with your actual API key if needed
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return data['rates']['ILS']

    def get_money_interval(self, amount):
        interval = (amount - (5 - self.difficulty), amount + (5 - self.difficulty))
        return interval

    def get_guess_from_user(self, amount):
        while True:
            try:
                guess = float(input(f"Guess the value of {amount} USD in ILS: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play(self):
        amount = random.randint(1, 100)
        interval = self.get_money_interval(amount * self.exchange_rate)
        guess = self.get_guess_from_user(amount)
        if interval[0] <= guess <= interval[1]:
            print("You won!")
        else:
            print("You lost!")

if __name__ == "__main__":
    difficulty = int(input("Enter difficulty: "))
    game = CurrencyRouletteGame(difficulty)
    game.play()