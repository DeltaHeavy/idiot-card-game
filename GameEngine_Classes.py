from random import shuffle # Shuffles the deck
from GameEngine_Functions import *

class Card:
    def __init__(self, name, value): # note that suits don't matter
        self.name, self.value = name, value # Names are like "2", "3", or "Ace"; Values are like 2, 3, or 14

class Deck:
    def __init__(self): # Build the deck
        self.cards = []
        for suit in range(4):
            for x in range(2, 11):
                self.cards.append(Card(name=str(x), value=x))
            names = ['Jack', 'Queen', 'King', 'Ace']
            for name in names:
                self.cards.append(Card(name=name, value=names.index(name)+11))
        shuffle(self.cards) # shuffle modifies in-place, no need to assign nor return

    def draw(self, count): # Draw int(count) cards from the deck
        drawn = []
        for x in range(count):
            drawn.append(self.cards.pop(0))
        return drawn

class Player: # Players can be human or ai

    count = 0 # for assigning player id (pid)
    human_pcount = 0 # for checking that there are at least 2 players
    cpu_pcount = 0 # and for naming cpus
    taken_names = [] # for keeping player names unique

    def __init__(self, is_human, deck):
        self.is_human = is_human
        if is_human:
            self.pid = Player.count
            self.name = get_name(Player.taken_names)
            Player.taken_names.append(self.name)
            Player.human_pcount+=1
        else:
            self.pid = Player.count
            self.name = "CPU-" + str(Player.cpu_pcount)
            Player.cpu_pcount+=1
        self.hand = deck.draw(3)
        self.faceups = deck.draw(3)
        self.facedowns = deck.draw(3)
        Player.count+=1

    def play_from_facedowns(self):
        return self.facedowns.pop()

    def play_from_faceups(self):
        return self.faceups.pop(choose(self.faceups.cards))

class Game:
    def __init__(self):
        self.winner = None
        self.players = []
        self.deck = Deck()
        self.pile = []
        human_pcount, cpu_pcount = get_player_counts()
        for x in range(human_pcount):
            self.players.append(Player(is_human=True, deck=self.deck))
        for x in range(cpu_pcount):
            self.players.append(Player(is_human=False, deck=self.deck))
        assert human_pcount+cpu_pcount == Player.count and Player.count <= 5

    def get_player(self, pid):
        for player in self.players:
            if player.pid == pid:
                return player

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
                    if len(player.hand)+len(player.facedowns) == 0:
                        winner = player
            except KeyboardInterrupt:
                print()
                return 1
        victory(player)
        return 0
