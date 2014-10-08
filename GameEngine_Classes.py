from random import shuffle # Shuffles the deck
from GameEngine_Functions import *
from GameEngine_AI import *

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

    def draw(self): # Draw a card from the deck
        return self.cards.pop(0)

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
            self.ai = AI()
        self.hand = []
        self.faceups = []
        self.facedowns = []
        for x in range(3):
            self.hand.append(deck.draw())
            self.faceups.append(deck.draw())
            self.facedowns.append(deck.draw())
        Player.count+=1

    def play(self, from_where, pile):
        assert from_where in ['hand', 'faceups', 'facedowns']
        if from_where == 'facedowns':
            return [self.facedowns.pop()]
        elif from_where == 'hand':
            cards = self.hand
        elif from_where == 'faceups':
            cards = self.faceups
        chosen_cards = []
        if not can_play(cards, pile):
            return chosen_cards
        if self.is_human:
            chosen_index = None
            while chosen_index is None:
                chosen_index = choose(cards)
                chosen_value = cards[chosen_index].value
                if playable(cards[chosen_index], pile):
                    count = 0
                    for card in cards:
                        if card.value == chosen_value:
                            count+=1
                    how_many = 1
                    if count > 1:
                        how_many = get_int_input(1, count, "How many would you like to play?")
                    index = 0
                    if from_where == 'hand':
                        while len(chosen_cards) < how_many:
                            if self.hand[index].value == chosen_value:
                                chosen_cards.append(self.hand.pop(index))
                            else:
                                index+=1
                    elif from_where == 'faceups':
                        while len(chosen_cards) < how_many:
                            if self.faceups[index].value == chosen_value:
                                chosen_cards.append(self.faceups.pop(index))
                            else:
                                index+=1
                    return chosen_cards
                else:
                    chosen_index = None
        else:
            return self.ai.ai_choose(cards, pile)

class Game:
    def __init__(self):
        self.winner = None
        self.deck = Deck()
        self.players = []
        self.pile = []
        human_pcount = get_int_input(0, 5, "How many human players? [0-5]")
        cpu_pcount = get_int_input(2-human_pcount if human_pcount < 2 else 0, 5-human_pcount, "How many cpu players?")
        for x in range(human_pcount):
            self.players.append(Player(is_human=True, deck=self.deck))
        for x in range(cpu_pcount):
            self.players.append(Player(is_human=False, deck=self.deck))
        assert human_pcount+cpu_pcount == Player.count and Player.count <= 5

    def pickup(self, player):
        display(player.name + " has to pick up the pile!")
        for x in range(len(self.pile)):
            player.hand.append(self.pile.pop())

    def blowup(self, name):
        display(name + " blew up the pile!")
        self.pile = []

    def turn(self, player):
        played = []
        if player.hand:
            player.hand = sort_cards(player.hand)
            played = player.play('hand', self.pile)
        elif player.faceups:
            played = player.play('faceups', self.pile)
        elif player.facedowns:
            played = player.play('facedowns', self.pile)
        if not played:
            self.pickup(player)
            return True
        while self.deck.cards and len(player.hand) < 3:
            player.hand.append(self.deck.draw())
        for card in played:
            self.pile.insert(0, card)
        if self.pile[0].value == 10:
            self.blowup(player.name)
            return False
        elif len(self.pile) >= 4: 
            if self.pile[0].value == self.pile[1].value == self.pile[2].value == self.pile[3].value:
                self.blowup(player.name)
                return False
        return True

    def main(self):
        while self.winner is None:
            try:
                for player in self.players:
                    turn_done = False
                    display(player.name + "'s turn:")
                    while not turn_done:
                        if not player.is_human:
                            player.ai.update(self)
                        turn_done = self.turn(player)
                    display("--------------------------------")
                    display_cards(self.pile)
                    display("--------------------------------")
                    if len(player.hand)+len(player.facedowns) == 0:
                        self.winner = player
            except KeyboardInterrupt:
                print()
                return 1
        display(self.winner.name + " is the winner!")
        return 0
