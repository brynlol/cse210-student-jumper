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
        letter (str): The user's guess will be stored here.
        word_line (str): The masked word will be stored here.
        console (Console): An instance of the class of objects known as Console.
        puzzle (Puzzle): An instance of the class of objects known as Puzzle.
        jumper (Jumper): An instance of the class of objects known as Jumper.
    """

    def __init__(self):
        self.keep_playing = True
        self.letter = ''
        self.word_line = ''
        self.console = Console() 
        self.puzzle = Puzzle()
        self.jumper = Jumper()
    
    def start_game(self):
        self.get_inputs()
        self.do_updates()
        self.do_outputs()

    def get_inputs(self):
        self.console.write_text(self.puzzle.get_word_progress())
        self.console.write_text(self.jumper.jumper_str())
        self.letter = self.console.get_string('Guess a letter [a-z]: ')
        

    def do_updates(self):
        if len(self.puzzle.chosen_word) >= 3 and  len(self.puzzle.chosen_word) < 7:
            self.jumper.num_lives = 5
        elif len(self.puzzle.chosen_word) >= 7 and  len(self.puzzle.chosen_word) < 11:
            self.jumper.num_lives = 7
        else:
            self.jumper.num_lives = 9
        if self.puzzle.store_guess(self.letter):
            self.word_line = self.puzzle.get_word_progress()
        else:
            self.jumper.lose_life() 
        

    def do_outputs(self):
        self.console.write_text(self.word_line)
        self.console.write_text(self.jumper.jumper_str())
        self.keep_playing = (self.jumper.num_lives > 0)

