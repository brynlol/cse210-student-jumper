class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """

    def get_letter(self):
        """Get a single character from the user.

        Returns:
            str: a single lowercase character.
        """
        valid_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        letter = ''
        while len(letter) != 1 and letter not in valid_letters:
            letter = input('Guess a letter [a-z]: ').lower()
        return letter
     
    def get_string(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def get_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            float: The user's input as a float.
        """
        return float(input(prompt))
        
    def write_text(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Console): An instance of Console.
            text (string): The text to display.
        """
        print(text)

    def write_list(self, list):
        """Displays a list using for loop to print it down a line.
        Args:
            self (Console): An instance of Console.
            list (list): The list to display down a line
        """

        for i in list:
            print(i)