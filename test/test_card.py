from project.card import Card
import pytest

class TestCard:
    def test_selected(self):
        new_card = Card(2, 1)
        assert new_card.selected() == 'Ace of Diamonds'
    
    def test_selected(self):
        new_card = Card(3, 9)
        assert new_card.selected() == '9 of Hearts'
        
    def test_selected_picture(self):
        new_card = Card(4, 12)
        assert new_card.selected() == 'Queen of Spades'
        
    def test_compare_exception(self):
        with pytest.raises(ValueError):
            Card(2, 9).compare(3)
        
    def test_compare_new_card_higher(self):
        # Arrange
        expected = 1
        
        # Act
        new_card = Card(3, 7)
        previous_card = Card(3, 5)
        
        # Assert
        assert expected == new_card.compare(previous_card)
        
    def test_compare_new_card_lower(self):
        # Arrange
        expected = -1
        
        # Act
        new_card = Card(1, 9)
        previous_card = Card(2, 11)
        
        # Assert
        assert expected == new_card.compare(previous_card)
        
    def test_compare_cards_with_same_pip_value_different_suits(self):
        # Arrange
        expected = -1
        
        # Act
        new_card = Card(1, 6)
        previous_card = Card(4, 6)
        
        # Assert
        assert expected == new_card.compare(previous_card)