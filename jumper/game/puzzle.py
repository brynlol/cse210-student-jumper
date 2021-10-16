import random
import linecache

class Puzzle:
    """Stores the puzzle and guesses.
    
    Stereotype:
        Information Holder

    Attributes:
        wordlist (str): path to list of words to use seperated by line breaks.
        min_word_chars (int): minimum word length to be guessed.
        wordlist_size (int): size of the word list in lines.
        chosen_word (str): current word to be guessed.
        previously_done_words (list): all words that were previously guessed
        guesses (list): all stored guesses

    """

    def __init__(self, wordlist='../data/mit-wordlist.txt', min_chars=2):
        """Initialize the puzzle with a given wordlist and minimum character filter.

        Args:
            wordlist (str, optional): Path to word list separated by line breaks. Defaults to '../data/mit-wordlist.txt'.
            min_chars (int, optional): Minimum amount of characters to use for a chosen word. Defaults to 2.
        """
        self.wordlist = wordlist
        self.min_word_chars = min_chars

        with open(wordlist, 'r') as wordlist_file:
            self.wordlist_size = len([0 for _ in wordlist_file])
        
        self.previously_done_words = []
        self.choose_new_word()

        self.guesses = []

    
    def choose_new_word(self):
        """Choose a fresh word from the word list.

        Tries not to repeat words, gives up at a certain point.
        """
        self.chosen_word = ''
        fresh_tries = 0
        while ((len(self.chosen_word) < self.min_word_chars) and
                (self.chosen_word not in self.previously_done_words) 
                and fresh_tries < len(self.previously_done_words) * 2 + 1):
            self.chosen_word = linecache.getline(self.wordlist, random.randint(0, self.wordlist_size - 1)).strip()
            fresh_tries += 1
        self.previously_done_words.append(self.chosen_word)

    def store_guess(self, guess):
        """Store user guess and determine whether it was correct.

        Args:
            guess (str): character being guessed.

        Returns:
            bool: True if guess is correct, false otherwise.
        """
        if len(guess) > 1:
            raise(ValueError('Guess must only contain one character.'))
        self.guesses.append(guess)
        if guess in self.chosen_word:
            return True
        return False

    def get_word_progress(self):
        """Build string showing how many characters are in the word reflecting the player's progress.

        Returns:
            str: string with guessed letters and underlines for unknown letters.
        """
        masked_string = ''
        for letter in self.chosen_word:
            if letter in self.guesses:
                masked_string += letter
            else:
                masked_string += '_'
            masked_string += ' '
        return masked_string.strip()
        