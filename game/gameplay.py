from game.cards import Cards

class Director:
    """A Person who directs the game.

    The Director class is responsible for controlling the action of the game
    Attributes:

        is_playing (boolean): whether or not the game is being played
        score(int): points earned or lost during a round
        total_score(int): total points for the game
    """

    def __init__(self):
        """Construction of a new instance of Director
        
        args:
            self(Director): an instance of Director
        
        """
        self.isplaying = True
        self.score = 300
        self.total_score = 0
        self.draw_card = 0
        self.guess_card = 0
        self.next_card = 0

        print("This is Hi-Lo, a guessing game of chance. You will be given a card, then you will guess if the next card will be higher or lower. A correct guess gets you 100 points, an incorrect guess loses you 75 points. You start the game with 300 points. Good Luck!")
       
        

    def play_game(self):
        """Starts the main game loop
        
        Args: 
            self(Director): an instance of Director"""
        while self.isplaying:
            self.getinput()
                


    def get_input(self):
        """Asks the user if they want to play
        
        Args: 
            self(Director): an instance of Director
        """
        self.draw_card = Cards()
        print(f"The card is : {self.draw_card}")
        self.guess_card = input("Higher or lower? (h/l)")
        self.next_card = Cards()

        
    def compare(self):
        """Compares the users guess to the cards drawn
        
        args:
            self(Director): an instance of Director
            """
        if self.next_card < self.draw_card:
            lower = True
        elif self.next_card > self.draw_card:
            higher = True
        
        if self.guess_card == "l" and lower:
            self.score += 100
        elif self.guess_card == "h" and higher:
            self.score += 100
        else:
            self.score -= 75
    
    def output(self):
        """Totals the points and gives the user the results
        
        Args:
            self(Director): an instance of Director
        """
        self.score += self.total_score
        print(f"Your score is: {self.total_score}")
        play_again = input("Would you like to play again? (y/n)")
        self.isplaying = (play_again == "y")
    