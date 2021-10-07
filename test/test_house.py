from project.house import House
import pytest

class TestHouse:
    def test_constructor(self):
        # Arrange
        expected_score = 100
        expected_bet = 100
        expected_minimum_bet = 50
        
        # Act
        house = House(100)
        
        # Assert
        assert expected_score == house.score()
        assert expected_bet == house.bet()
        assert expected_minimum_bet == house.minimum_bet()
        
    def test_make_bet_too_high(self):
        # Arrange
        house = House(100)
        
        # Exception
        with pytest.raises(ValueError):
            house.make_bet(101)
            
    def test_make_bet_too_low(self):
        # Arrange
        house = House(100)
        
        # Exception
        with pytest.raises(ValueError):
            house.make_bet(49)
            
    def test_make_bet(self):
        # Arrange
        expected = 75
        house = House(100)
        
        # Act
        house.make_bet(75)
        
        # Assert
        assert expected == house.bet()
        
    def test_update_score_wins(self):
        # Arrange
        expected_score = 175
        expected_minimum_bet = 87
        
        house = House(100)
        house.make_bet(75)
        
        # Act
        actual_score = house.update_score(True)
        
        # Assert
        assert expected_score == actual_score
        assert expected_minimum_bet == house.minimum_bet()
        
    def test_update_score_loses(self):
        # Arrange
        expected_score = 25
        expected_minimum_bet = 12
        
        house = House(100)
        house.make_bet(75)
        
        # Act
        actual_score = house.update_score(False)
        
        # Assert
        assert expected_score == actual_score
        assert expected_minimum_bet == house.minimum_bet()