import random

class Cards:
    """A self to hold the cards used for the Hilo game
    
    Attributes:
        number (int): the number of the card that is drawn
        
    """

    def __init__(self):
        """Construction of a new instance of Cards
        
        args:
            self(Cards): an instance of Cards
        
        """
        self.number = 0
        

    def draw_card(self):
        """A method to randomly draw the next card for the player
        
        args:
            self (Cards): an instance of Cards
        
        """
        self.number = random.randint(1,13)
        return self.number
