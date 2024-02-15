import random

class Card:
    
    def __init__(self, suit, value ):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return '{}-->{}'.format(self.suit, self.value)

class deck:
    def __init__(self):
        suits = ['hearts','diamond','clubs', 'spades']
        values = ['A','2','3','4','5','6','7','8','9','10','K','Q','J']
        self.cards = [Card(suit,value) for suit in suits for value in values]

    def __str__(self):
        return 'cards left ' + str(len(self.cards))

    def shuffle(self):
        if len(self.cards)<52:
            print('only full deck can be shuffled')
        else:
            random.shuffle(self.cards)
        return self.cards
    def deal(self):
        if len(self.cards) == 0:
            print('all cards has been dealt')
        return self.cards.pop()    


deck = deck()
deck.shuffle()
print(deck.deal())   
print(deck.deal())  
print(deck)  
