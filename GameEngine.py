from random import shuffle

class Card:
    def __init__(self, name, value):
        self.name, self.value = name, value

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for x in range(2, 11):
                self.cards.append(Card(name=str(x), value=x))
            names = ['Jack', 'Queen', 'King', 'Ace']
            for name in names:
                self.cards.append(Card(name=n, value=names.index[name]+11))
        shuffle(self.cards)

    def draw(self, count):
        drawn = []
        for x in range(count):
            drawn.append(self.cards.pop(0))
        return drawn

class Pile:
    def __init__(self):
        self.cards = []

class Three:
    def __init__(self, deck):
        self.cards = deck.draw(3)

class Player:
    count = 0
    def __init__(self, is_human, deck):
        self.pid = Player.count
        Player.count+=1
        self.is_human = is_human
        self.hand = Three(deck)
        self.faceups = Three(deck)
        self.facedowns = Three(deck)

class Human(Player):
    pass # TODO

class Cpu(Player):
    pass # TODO
