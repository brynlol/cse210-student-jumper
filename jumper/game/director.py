from game.console import Console
from game.puzzle import Puzzle
from game.processor import Processor

class Director:

    def __init__(self):
       pass
    
    def start_game(self):
        self.get_inputs()
        self.do_updates()
        self.get_outputs()

    def get_inputs(self):
        pass

    def do_updates(self):
        pass

    def get_outputs(self):
        pass