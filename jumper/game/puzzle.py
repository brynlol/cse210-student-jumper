import random

class Puzzle:


    def __init__(self):

        words = ["random", "horse", "computer", "recreation", "scriptures", "family", "gratitude", "creation", "unity", "fantastic", "growth", "majesty", "mountain", "ocean", "basket"]
        self.word = random.choice(words)

    def get_word_line(self):
        pass

    def get_jumper(self):
        jumper = [" _____","/_____\\","\\     /"," \\   /", "   0", "  /|\\", "  / \\"]
        return jumper
