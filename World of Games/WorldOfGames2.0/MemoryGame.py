# MemoryGame.py
import random
import time


class MemoryGame:
    def __init__(self, player_name, difficulty):
        """
        Initialize the Memory Game with the player's name and difficulty level.
        Generates a sequence of random numbers based on the difficulty level.

        :param player_name: str - The name of the player.
        :param difficulty: int - The difficulty level chosen by the player.
        """
        self.player_name = player_name
        self.difficulty = difficulty
        self.sequence = self.generate_sequence()

    def generate_sequence(self):
        """
        Generate a sequence of random numbers based on the difficulty level.

        :return: list - A list of random numbers with a length equal to the difficulty level.
        """
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        """
        Prompt the player to input the sequence of numbers they remember.

        :return: list - A list of numbers input by the player.
        """
        print(f"{self.player_name}, please enter the {self.difficulty} numbers you remember:")
        user_sequence = []
        for _ in range(self.difficulty):
            num = input()
            # Validate the input to ensure it is a number
            while not num.isdigit():
                num = input("Invalid input. Please enter a number: ")
            user_sequence.append(int(num))
        return user_sequence

    def is_list_equal(self, user_sequence):
        """
        Compare the generated sequence with the player's input sequence.

        :param user_sequence: list - The list of numbers input by the player.
        :return: bool - True if the sequences match, False otherwise.
        """
        return self.sequence == user_sequence

    def play(self):
        """
        Play the Memory Game. Displays the sequence, waits for a short period,
        clears the screen, and then prompts the player to input the sequence.

        :return: bool - True if the player correctly remembers the sequence, False otherwise.
        """
        print("Remember the following sequence:")
        print(self.sequence)
        time.sleep(0.7)  # Display the sequence for 0.7 seconds
        self.clear_screen()  # Clear the screen to hide the sequence
        user_sequence = self.get_list_from_user()  # Get the sequence from the player
        return self.is_list_equal(user_sequence)  # Compare the sequences

    @staticmethod
    def clear_screen():
        """
        Clear the console screen by printing multiple new lines.
        """
        print("\n" * 100)