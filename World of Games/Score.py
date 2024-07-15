# Score.py

from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(game, difficulty):
    try:
        points_of_winning = (difficulty * 3) + 5
        print(f"Adding score: {points_of_winning} to {game}")  # Debugging statement
        try:
            # Try to read the current scores from the file
            with open(SCORES_FILE_NAME, 'r') as score_file:
                scores = eval(score_file.read().strip())
        except (FileNotFoundError, ValueError):
            # If the file does not exist or is empty, start with an empty dictionary
            scores = {"MemoryGame": 0, "GuessGame": 0, "CurrencyRouletteGame": 0}

        # Update the score for the specified game
        scores[game] += points_of_winning

        # Write the new scores to the file
        with open(SCORES_FILE_NAME, 'w') as score_file:
            score_file.write(str(scores))

        print(f"Updated scores: {scores}")  # Debugging statement
    except Exception as e:
        print(f"Error in add_score: {e}")  # Debugging statement
        return BAD_RETURN_CODE