# Live.py

# Import game classes from their respective modules
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame


# Function to welcome the player
def welcome(name):
    """
    Generate a welcome message for the player.

    :param name: str - The name of the player.
    :return: str - The welcome message.
    """
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


# Function to clear the console screen
def clear_screen():
    """
    Clear the console screen by printing multiple new lines.
    """
    print("\n" * 100)


# Function to load the game menu and handle game selection and difficulty
def load_game(player_name):
    """
    Display the game menu, handle game selection, and start the selected game.
    Allows the player to choose a game, set the difficulty, and play the game.
    Also allows the player to retry the game or return to the main menu after playing.

    :param player_name: str - The name of the player.
    """
    last_game = None
    last_difficulty = None

    while True:
        clear_screen()
        if last_game is None:
            # Display the game menu
            print("Please choose a game to play:")
            print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
            print("2. Guess Game - guess a number and see if you chose like the computer")
            print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
            print("q. Quit")

            # Get the player's choice of game
            game_choice = input("Enter the number of the game you want to play: ").strip().lower()
            if game_choice == 'q':
                exit("Quitting the World of Games. Goodbye!")
            while not game_choice.isdigit() or not (1 <= int(game_choice) <= 3):
                game_choice = input(
                    "Invalid input. Please enter a number between 1 and 3 (or 'q' to quit): ").strip().lower()
                if game_choice == 'q':
                    exit("Quitting the World of Games. Goodbye!")

            # Get the player's chosen difficulty level
            difficulty = input("Please choose game difficulty from 1 to 5: ").strip().lower()
            if difficulty == 'q':
                exit("Quitting the World of Games. Goodbye!")
            while not difficulty.isdigit() or not (1 <= int(difficulty) <= 5):
                difficulty = input("Invalid input. Please enter a number between 1 and 5: ").strip().lower()
                if difficulty == 'q':
                    exit("Quitting the World of Games. Goodbye!")

            game_choice = int(game_choice)
            difficulty = int(difficulty)
            last_game = game_choice
            last_difficulty = difficulty
        else:
            game_choice = last_game
            difficulty = last_difficulty

        # Initialize the chosen game with the given difficulty
        if game_choice == 1:
            game = MemoryGame(player_name, difficulty)
        elif game_choice == 2:
            game = GuessGame(player_name, difficulty)
        elif game_choice == 3:
            game = CurrencyRouletteGame(player_name, difficulty)

        # Play the game and check if the player won or lost
        if game.play():
            print(f"{player_name}, you won!")
        else:
            print(f"{player_name}, you lost!")

        # Ask the player if they want to retry or return to the main menu
        if not play_again():
            last_game = None
        else:
            print("Restarting the last game...")


# Function to ask the player if they want to play again or return to the main menu
def play_again():
    """
    Prompt the player to retry the last game, return to the main menu, or quit.

    :return: bool - True if the player wants to retry the game, False if they want to return to the main menu.
    """
    while True:
        choice = input(
            "Do you want to retry the last game or return to the main menu? (r: retry, m: main menu, q: quit): ").strip().lower()
        if choice == 'r':
            clear_screen()
            return True
        elif choice == 'm':
            clear_screen()
            return False
        elif choice == 'q':
            exit("Quitting the World of Games. Goodbye!")
        else:
            print("Invalid choice. Please enter 'r' to retry, 'm' to return to the main menu, or 'q' to quit.")