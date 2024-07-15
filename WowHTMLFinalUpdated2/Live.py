from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game(player_name):
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    print("q. Quit")

    game_choice = input("Enter the number of the game you want to play: ")
    if game_choice == 'q':
        return

    if game_choice not in ['1', '2', '3']:
        print("Invalid choice, please choose a valid game.")
        return

    difficulty = input("Please choose game difficulty from 1 to 5: ")
    if difficulty not in ['1', '2', '3', '4', '5']:
        print("Invalid difficulty level, please choose a valid level.")
        return

    difficulty = int(difficulty)

    if game_choice == '1':
        game = MemoryGame(player_name, difficulty)
        game_name = "MemoryGame"
    elif game_choice == '2':
        game = GuessGame(player_name, difficulty)
        game_name = "GuessGame"
    elif game_choice == '3':
        game = CurrencyRouletteGame(player_name, difficulty)
        game_name = "CurrencyRouletteGame"

    if game.play():
        print("You won!")
        # Assuming add_score function to update scores is implemented somewhere
        # add_score(game_name, difficulty)
    else:
        print("You lost!")