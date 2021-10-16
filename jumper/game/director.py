from game.console import Console
from game.puzzle import Puzzle
from game.jumper import Jumper

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        keep_playing (boolean): Whether or not the game can continue.
        console (Console): An instance of the class of objects known as Console.
        puzzle (Puzzle): An instance of the class of objects known as Puzzle.
        jumper (Jumper): An instance of the class of objects known as Jumper.
    """

    def __init__(self):
        self.keep_playing = True
        self.console = Console() 
        self.puzzle = Puzzle()
        self.jumper = Jumper()
    
    def start_game(self):
        self.get_inputs()
        self.do_updates()
        self.get_outputs()

    def get_inputs(self):

        letter = self.console.get_string("Guess a letter [a-z]: ")

    def do_updates(self):
        pass

    def get_outputs(self):
        pass