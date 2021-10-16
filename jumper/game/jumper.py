class Jumper:
    """Stores the lives and structure of the jumping man.
    
    Stereotype:
        Information Holder

    Attributes:
        num_lives (int): The number of lives the Jumper has.
        max_para (int): maximum spaces in the parachute.
        jumpman (tuple): The list representation of the jumping man.

    """
    
    def __init__(self, num_lives=3):
        """Initialize the jumpman with the configured lives.

        Args:
            num_lives (int, optional): total number of lives until game over. Defaults to the minimum of 3.
        """
        if num_lives < 3:
            raise(ValueError('Jumper cannot have less than 3 lives.'))
        self.num_lives = num_lives
        self.max_para = 2 * num_lives - 3
        self.build_jumper()


    def align(self, used_space, char=' '):
        """Align jumpman based on maximum and used space.

        Args:
            used_space (int): number of characters in used space.
            char (str, optional): character used to align. Defaults to ' '.

        Returns:
            str: alignment string to be concatnated.
        """
        num_align = (self.max_para - used_space) / 2
        return char * int(num_align)

    def build_jumper(self):
        """Builds the jumpman based on the number of lives and stores it in a tuple.
        """
        jumpman = []
        jumpman.append(' ' + '_' * self.max_para)
        jumpman.append('/' + '_' * self.max_para +'\\')
        for spaces in range(self.max_para, 1, -2):
            align = self.align(spaces)
            jumpman.append(align + '\\' + ' ' * spaces + '/')
        
        jumpman.append(self.align(-1) + '0')
        jumpman.append(self.align(1) + '/|\\')
        jumpman.append(self.align(1) + '/ \\')
        jumpman.append('\n')
        jumpman.append('^' * (self.max_para + 2))
        self.jumpman = tuple(jumpman)
    
    def jumper_str(self):
        """Turns the jumpman into a string.

        Returns:
            str: formatted jumpman for printing.
        """
        jump = '\n'
        for line in self.jumpman:
            jump += line + '\n'
        return jump
    
    def lose_life(self):
        """Change how the jumpman is displayed and decrement the number of lives by one.

        Returns:
            int: number of lives the jumpman has left.
        """

        def remove_top_layer(line):
            """Remove the top layer of the jumpman.

            Intended for use with filter.

            Args:
                line (str): line in jumpman tuple.

            Returns:
                bool: determine whether to omit the line or not.
            """
            if line == self.jumpman[0]:
                return False
            return True
        
        def change_head(line):
            """Check whether to use the normal or dead head on jumpman.

            Args:
                line (str): line in jumpman.

            Returns:
                str: part of the jumpman tuple.
            """
            if line[-1] == '0':
                return line[:-1] + 'X'
            return line

        self.num_lives -= 1
        self.jumpman = tuple(filter(remove_top_layer, self.jumpman))
        if self.num_lives == 0:
            self.jumpman = tuple(map(change_head, self.jumpman))
        return self.num_lives