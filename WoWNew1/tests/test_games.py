# tests/test_games.py

import unittest
from games.game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        game = Game("Test Game")
        self.assertEqual(game.name, "Test Game")

    def test_game_start_not_implemented(self):
        game = Game("Test Game")
        with self.assertRaises(NotImplementedError):
            game.start()

if __name__ == "__main__":
    unittest.main()