# games/game.py

class Game:
    def __init__(self, name):
        self.name = name

    def start(self):
        raise NotImplementedError("You must implement the start method for the game.")