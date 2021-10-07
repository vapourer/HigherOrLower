from project.suit import Suit

class Card:
    """Representation of a playing card.
    
    Arguments:
    suit -- set according to the Suit enum value.
    pips -- can take values 1 - 13, with 11, 12 and 13 identifying the pictures.
    
    Attributes:
    __suit -- the Suit enum value.
    __pips -- the pips value.  Ace is low.
    """
    
    def __init__(self, suit: Suit, pips: int):
        self.__suit = Suit(suit)
        self.__pips = pips

    def __card_value(self):
        if (self.__pips == 1):
            return 'Ace'
        elif (self.__pips <= 10):
            return str(self.__pips)
        elif (self.__pips == 11):
            return 'Jack'
        elif (self.__pips == 12):
            return 'Queen'
        else:
            return 'King'
            
    def selected(self):
        """String representation of the card"""
        return self.__card_value() + ' of ' + self.__suit.name
        
    def compare(self, other) -> int:
        """Compares two Card instances
        
        Arguments:
        other -- card to be compared with current card
        
        Returns:
        int -- -1 if self < other; 1 if self > 0
        """
        
        if (isinstance(other, Card)):
            return self.__compare(other)
        else:
            raise ValueError('other must be a playing card')
            
    def __compare(self, other) -> int:
        if (self.__pips < other.__pips):
            return -1
        elif (self.__pips > other.__pips):
            return 1
        else:
            return self.__compare_suits(self.__suit, other.__suit)
            
    def __compare_suits(self, suit_a: Suit, suit_b: Suit) -> int:
        if (suit_a.value < suit_b.value):
            return -1
            
        return 1