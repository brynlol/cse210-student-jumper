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
        masked_word (str): The masked word will be stored here.
        console (Console): An instance of the class of objects known as Console.
        puzzle (Puzzle): An instance of the class of objects known as Puzzle.
        jumper (Jumper): An instance of the class of objects known as Jumper.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Director): An instance of Director.
        """

        self.keep_playing = True
        self.letter = ''
        self.masked_word = ''
        self.console = Console() 
        self.puzzle = Puzzle()
        #Determine how many lives the user will get.
        if len(self.puzzle.chosen_word) >= 3 and  len(self.puzzle.chosen_word) < 7:
            num_lives = 7
        elif len(self.puzzle.chosen_word) >= 7 and  len(self.puzzle.chosen_word) < 11:
            num_lives = 9
        else:
            num_lives = 11
        self.jumper = Jumper(num_lives) #pass in the number of lives the user gets

    
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """

        self.console.write_text(self.puzzle.get_word_progress())
        self.console.write_text(self.jumper.jumper_str())
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the users next guess.

        Args:
            self (Director): An instance of Director.
        """       
        self.letter = self.console.get_letter()
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the user's guess gets checked. 
        If it is in the word, it gets added to the masked word.
        If it is not, they lose a life.

        Args:
            self (Director): An instance of Director.
        """
        guess_correct = self.puzzle.store_guess(self.letter)
        self.masked_word = self.puzzle.get_word_progress()
        if (not guess_correct) and (self.letter not in self.puzzle.guesses[:-1]):
            self.jumper.lose_life() 
        

    def do_outputs(self):
        """Updates the important game information for each round of play. In 
        this case, that means the masked word with any correct guesses is shown. 
        The jumper is shown and the number of lives are tracked 

        Args:
            self (Director): An instance of Director.
        """

        self.console.write_text(self.masked_word)
        self.console.write_text(self.jumper.jumper_str())
        if self.jumper.num_lives <= 0:
            self.keep_playing = False
            self.console.write_text(f'The word was: {self.puzzle.chosen_word}. Better luck next time!')
        elif self.puzzle.check_word_completion(self.masked_word) == True:
            self.keep_playing = False
            self.console.write_text('You guessed it! Great Work!')
        else:
            self.keep_playing = True


