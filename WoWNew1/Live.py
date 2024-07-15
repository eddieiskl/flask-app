# Live.py

import subprocess

def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 0.7 seconds and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    while True:
        try:
            game_choice = int(input("Enter the number of the game you want to play (1-3): "))
            if game_choice not in [1, 2, 3]:
                print("Invalid choice. Please choose a number between 1 and 3.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if difficulty not in [1, 2, 3, 4, 5]:
                print("Invalid choice. Please choose a number between 1 and 5.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    if game_choice == 1:
        game = "memory-game"
        script = "MemoryGame.py"
    elif game_choice == 2:
        game = "guess-game"
        script = "GuessGame.py"
    else:
        game = "currency-roulette-game"
        script = "CurrencyRouletteGame.py"

    print(f"Starting {game} with difficulty {difficulty}...")
    result = subprocess.run(["docker-compose", "run", "--rm", game, "sh", "-c", f"python3 {script} {difficulty}"])
    if result.returncode != 0:
        print(f"Failed to start {game} container.")
    else:
        print(f"{game} container started successfully.")

if __name__ == "__main__":
    print(welcome("Guy"))
    load_game()