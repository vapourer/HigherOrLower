from project.pack import Pack
import project.card
import pytest
import random

class TestPack:        
    def test_shuffle_incorrect_length_argument(self):
        # Arrange
        pack = Pack()
        random_order = [n for n in range(53)]
        random.shuffle(random_order)
        
        # Exception
        with pytest.raises(ValueError):
            pack.shuffle(random_order)
        
    def test_shuffle(self):
        # Arrange
        expected = []
        expected.append('2 of Diamonds')
        expected.append('6 of Diamonds')
        expected.append('King of Spades')
        expected.append('5 of Spades')
        expected.append('4 of Spades')
        expected.append('King of Clubs')
        expected.append('5 of Hearts')
        expected.append('8 of Clubs')
        expected.append('10 of Hearts')
        expected.append('10 of Clubs')
        expected.append('7 of Clubs')
        expected.append('Queen of Clubs')
        expected.append('6 of Spades')
        expected.append('3 of Hearts')
        expected.append('8 of Hearts')
        expected.append('Ace of Diamonds')
        expected.append('6 of Hearts')
        expected.append('7 of Diamonds')
        expected.append('Queen of Diamonds')
        expected.append('4 of Hearts')
        expected.append('9 of Spades')
        expected.append('4 of Clubs')
        expected.append('Ace of Clubs')
        expected.append('8 of Spades')
        expected.append('2 of Clubs')
        expected.append('2 of Hearts')
        expected.append('8 of Diamonds')
        expected.append('7 of Hearts')
        expected.append('7 of Spades')
        expected.append('5 of Diamonds')
        expected.append('Ace of Spades')
        expected.append('3 of Clubs')
        expected.append('3 of Diamonds')
        expected.append('10 of Diamonds')
        expected.append('9 of Clubs')
        expected.append('4 of Diamonds')
        expected.append('5 of Clubs')
        expected.append('3 of Spades')
        expected.append('Queen of Spades')
        expected.append('Jack of Diamonds')
        expected.append('9 of Diamonds')
        expected.append('Jack of Spades')
        expected.append('King of Hearts')
        expected.append('2 of Spades')
        expected.append('King of Diamonds')
        expected.append('10 of Spades')
        expected.append('Jack of Hearts')
        expected.append('Ace of Hearts')
        expected.append('6 of Clubs')
        expected.append('Queen of Hearts')
        expected.append('Jack of Clubs')
        expected.append('9 of Hearts')
        
        random_order = []
        random_order.append(14)
        random_order.append(18)
        random_order.append(51)
        random_order.append(43)
        random_order.append(42)
        random_order.append(12)
        random_order.append(30)
        random_order.append(7)
        random_order.append(35)
        random_order.append(9)
        random_order.append(6)
        random_order.append(11)
        random_order.append(44)
        random_order.append(28)
        random_order.append(33)
        random_order.append(13)
        random_order.append(31)
        random_order.append(19)
        random_order.append(24)
        random_order.append(29)
        random_order.append(47)
        random_order.append(3)
        random_order.append(0)
        random_order.append(46)
        random_order.append(1)
        random_order.append(27)
        random_order.append(20)
        random_order.append(32)
        random_order.append(45)
        random_order.append(17)
        random_order.append(39)
        random_order.append(2)
        random_order.append(15)
        random_order.append(22)
        random_order.append(8)
        random_order.append(16)
        random_order.append(4)
        random_order.append(41)
        random_order.append(50)
        random_order.append(23)
        random_order.append(21)
        random_order.append(49)
        random_order.append(38)
        random_order.append(40)
        random_order.append(25)
        random_order.append(48)
        random_order.append(36)
        random_order.append(26)
        random_order.append(5)
        random_order.append(37)
        random_order.append(10)
        random_order.append(34)
        
        # Act
        shuffled_pack = Pack().shuffle(random_order)
        actual = [card.selected() for card in shuffled_pack]
        
        # Assert
        assert expected == actual