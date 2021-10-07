from project.card import Card

class Pack:
    """An unshuffled pack of cards.
    
    Attributes:
    __new -- the new pack as a list.
    """
    
    def __init__(self):
        self.__new = [Card(x, y) for x in range(1, 5) for y in range(1, 14)]
        
    def shuffle(self, random_order: list) -> list:
        """Shuffles this pack according to random_order.
        
        Arguments:
        random_order -- list of integers.
        
        Returns:
        The shuffled pack as a list.
        
        Exception:
        ValueError -- if random_order not size of a standard pack.
        """
        
        if (len(random_order) != len(self.__new)):
            raise ValueError('random_order must be exactly the size of a standard pack')
        
        return [self.__new[i] for i in random_order]
        