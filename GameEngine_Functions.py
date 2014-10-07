from Interface import *

def get_input(message=None):
    if message:
        display(message)
    return input()

def get_int_input(low, high, message=None):
    choice = None
    while choice is None:
        try:
            choice = int(get_input(message))
            if choice not in range(low, high+1):
                raise ValueError
        except:
            display("Invalid input. Enter a number from " + str(low) + " to " + str(high) + ".")
            choice = None
    return choice

def get_name(taken_names):
    name = None
    while not name:
        try:
            name = get_input("Please enter your name.")
            if name in taken_names:
                raise ValueError
        except ValueError:
            display("That name is taken.")
            name = None
    return name

def playable(card, pile):
    if not pile or card.value == 2 or card.value == 10:
        return True
    topcard_v = pile[0].value
    if topcard_v == 7:
        if card.value <= 7:
            return True
    elif card.value >= topcard_v:
        return True
    display(card.name + " can't play on " + pile[0].name)
    return False

def can_play(cards, pile):
    if not pile:
        return True
    values = [card.value for card in cards]
    if 10 in values or 2 in values:
        return True
    topcard_v = pile[0].value
    if topcard_v == 7:
        for x in range(len(cards)):
            if values[x] <= 7:
                return True
    else:
        for x in range(len(cards)):
            if values[x] >= topcard_v:
                return True
    return False

def blowup(name):
    display(name + " blew up the pile!")
    return []

def choose(cards):
    display("Pick a card to play.")
    display_cards(cards)
    return get_int_input(0, len(cards)-1)

def sort_cards(cards):
    return sorted(cards, key=lambda card: card.value)

def victory(player):
    display(player.name + "is the winner!")
