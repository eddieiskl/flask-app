# CurrencyRouletteGame.py
import random
import requests

class CurrencyRouletteGame:
    def __init__(self, player_name, difficulty):
        self.player_name = player_name
        self.difficulty = difficulty

    # Get the interval and actual value of the currency conversion
    def get_money_interval(self, amount):
        # Fetch the current exchange rate from USD to ILS
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        rate = response.json().get('rates').get('ILS')
        # Calculate the total value in ILS
        total_value = amount * rate
        # Calculate the interval based on difficulty
        lower_bound = total_value - (5 - self.difficulty)
        upper_bound = total_value + (5 - self.difficulty)
        return lower_bound, upper_bound, total_value

    # Get the player's guess for the currency conversion
    def get_guess_from_user(self, amount):
        guess = input(f"{self.player_name}, guess the value of {amount} USD in ILS: ")
        while not guess.replace('.', '', 1).isdigit():
            guess = input("Invalid input. Please enter a number: ")
        return float(guess)

    # Play the Currency Roulette Game
    def play(self):
        # Generate a random USD amount between 1 and 100
        amount = random.randint(1, 100)
        # Get the acceptable interval and actual total value in ILS
        interval = self.get_money_interval(amount)
        # Get the player's guess
        guess = self.get_guess_from_user(amount)
        # Check if the guess is within the interval
        if interval[0] <= guess <= interval[1]:
            return True
        else:
            # If the guess is incorrect, print the correct value
            print(f"Sorry, {self.player_name}. The correct value was {interval[2]:.2f} ILS.")
            return False