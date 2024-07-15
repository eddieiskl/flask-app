# Live.py
from GuessGame import play as guess_game_play

def welcome():
    print("Welcome to the World of Games (WoG). Here you can find many cool games to play.")

def load_game():
    print("Loading game...")
    guess_game_play()

if __name__ == "__main__":
    welcome()
    load_game()