import random
from project.pack import Pack
from project.card import Card
from project.house import House

# Not a game I knew.
# Loosely based on https://www.mathsisfun.com/games/higher-or-lower.html.

__history = []

def shuffled_pack():
    random_order = [x for x in range(52)]
    random.shuffle(random_order)
    return Pack().shuffle(random_order)
    
def place_bet(house: House):
    bet = 0
    
    while (bet < house.minimum_bet() or bet > house.score()):
        bet_as_string = input('Place a bet between ' + str(house.minimum_bet()) + ' and ' + str(house.score()) + ': ')
        
        if (bet_as_string.isnumeric()):
            bet = int(bet_as_string)
        else:
            bet = 0
        
    house.make_bet(bet)
    print('You have bet ' + str(house.bet()))
    print()
    
def make_play(pack: Pack) -> bool:
    decision = 'x'
    expectation = 0
    wins = False
    
    while (decision != 'h' and decision != 'l'):
        decision = input('Higher (h) or Lower (l)? ')
        
    if (decision == 'h'):
        print("You have selected 'Higher'")
        expectation = 1
    else:
        print("You have selected 'Lower'")
        expectation = -1
    
    print()
    
    last_card_index = len(__history) - 1
    previous_card = __history[last_card_index]    
    current_card = pack.pop()
    print(current_card.selected() + ' plays ' + previous_card.selected())    
    
    wins = current_card.compare(previous_card) == expectation
    __history.append(current_card)
        
    return wins

def play():
    initial_score = 100
    draw_count = 4
    
    house = House(initial_score)
    print('Initial score is ' + str(house.score()))
    print()
    
    pack = shuffled_pack()
    current_card = pack.pop()
    __history.append(current_card)
    
    while (house.score() > 0 and draw_count > 0):
        print('History')
        for card in __history:
            print(card.selected())
        print()
    
        place_bet(house)
        wins = make_play(pack)
        print('Wins: ' + str(wins))
    
        new_score = house.update_score(wins)
        print('Score is now ' + str(new_score))
        print()
        
        draw_count -= 1
       
    if (house.score() == 0):
        print("Oops!")
    elif (house.score() <= initial_score):
        print("Could be worse.")
    else:
        print("Well done!")
    
play()