class House:
    """A House instance maintains score and provides opportunity to bet.
    
    Arguments:
    initial_score -- sets the opening score as an int
    
    Attributes:
    __score -- maintains the current score
    __bet -- accepts a bet as an int.  Maximum available = current score.
    __minimum_bet = minimum allowable bet = half of current score.
    """
    def __init__(self, initial_score: int):
        self.__score = initial_score
        self.__bet = self.__score
        self.__minimum_bet = self.__score // 2
        
    def score(self):
        """The current score."""
        return self.__score
        
    def bet(self):
        """Placed bet."""
        return self.__bet
        
    def minimum_bet(self):
        """Minimum available bet."""
        return self.__minimum_bet
        
    def make_bet(self, bet: int):
        """Place a bet
        
        Arguments:
        bet -- as an int value (minimum_bet <= bet <= score)
        
        Exceptions:
        ValueError -- bet is outside allowed range
        """
        
        if (bet > self.__score):
            raise ValueError('bet must be less than or equal current score')
            
        if (bet < self.__minimum_bet):
            raise ValueError('bet must be at least half of current score')
            
        self.__bet = bet
    
    def update_score(self, wins: bool) -> int:
        """Adjusts the current score according to last result.
        
        Arguments:
        wins -- as a Boolean
        
        Returns:
        updated score as an int
        """
        
        if (wins):
            self.__score += self.__bet
            self.__minimum_bet = self.__score // 2
        else:
            self.__score -= self.__bet
            self.__minimum_bet = self.__score // 2
            
        return self.__score
        