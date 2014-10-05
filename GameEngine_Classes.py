from random import shuffle
from GameEngine_Functions import *

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
                self.cards.append(Card(name=name, value=names.index(name)+11))
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
    human_pcount = 0
    cpu_pcount = 0
    def __init__(self, is_human, deck):
        self.is_human = is_human
        if is_human:
            self.pid = Player.count
            self.name = get_name()
            Player.human_pcount+=1
        else:
            self.pid = Player.count
            self.name = "CPU-" + str(Player.cpu_pcount)
            Player.cpu_pcount+=1
        self.hand = Three(deck)
        self.faceups = Three(deck)
        self.facedowns = Three(deck)
        Player.count+=1

    def play_from_facedowns(self):
        return self.facedowns.cards.pop()

    def play_from_faceups(self):
        return self.faceups.cards.pop(choose(self.faceups.cards))

class Game:
    def __init__(self):
        self.winner = None
        self.players = []
        self.deck = Deck()
        self.pile = Pile()
        human_pcount, cpu_pcount = get_player_counts()
        for x in range(human_pcount):
            self.players.append(Player(is_human=True, deck=self.deck))
        for x in range(cpu_pcount):
            self.players.append(Player(is_human=False, deck=self.deck))
        assert human_pcount+cpu_pcount == Player.count and Player.count <= 5

    def human_turn(self, player):
        pass # TODO

    def cpu_turn(self, player):
        pass # TODO

    def main(self):    
        while self.winner is None:
            try:
                for player in self.players:
                    if player.is_human:
                        self.human_turn(player)
                    else:
                        self.cpu_turn(player)
                    if len(player.hand.cards)+len(player.facedowns.cards) == 0:
                        winner = player
            except KeyboardInterrupt:
                print()
                return 1
        victory(player)
        return 0
