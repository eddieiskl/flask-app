# MainGame.py

# Import the necessary functions from Live.py
from Live import load_game, welcome, clear_screen

# The entry point of the program
if __name__ == "__main__":
    # Prompt the player to enter their name
    player_name = input("Please enter your name: ").strip()
    # Allow the player to quit before starting the game
    if player_name.lower() == 'q':
        exit("Quitting the World of Games. Goodbye!")

    # Main game loop
    while True:
        clear_screen()
        # Display a welcome message to the player
        print(welcome(player_name))
        # Load the game menu and start the game
        load_game(player_name)
        # After playing, ask if the player wants to exit
        choice = input("Do you want to exit the World of Games? (y/n/q): ").strip().lower()
        if choice in ['y', 'q']:
            exit("Quitting the World of Games. Goodbye!")
        clear_screen()