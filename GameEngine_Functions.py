# Game Engine Functions
from Interface import *
from sys import exit

def get_input(message=None): # Getting string and integer inputs
    if message:
        display(message)
    return getinput()

def get_int_input(low, high, message=None): # Getting specifically integer inputs (within a range)
    choice = None
    while choice is None:
        try:
            choice = int(get_input(message))
            if choice not in range(low, high+1):
                raise ValueError
        except KeyboardInterrupt:
            print()
            exit(1)
        except ValueError:
            display("Invalid input. Enter a number from " + str(low) + " to " + str(high) + ".")
            choice = None
    return choice

def get_name(taken_names): # Naming human players
    name = None
    while not name:
        try:
            name = get_input("Please enter your name.")
            if name in taken_names:
                raise ValueError
        except KeyboardInterrupt:
            print()
            exit(1)
        except ValueError:
            display("That name is taken.")
            name = None
    return name

def can_play(cards, pile): # Playable in list(cards)
    if not cards:
        return False
    if not pile:
        return True
    for c in cards:
        if c.value == 10 or c.value == 2:
            return True
    topcard_v = pile[0].value
    if topcard_v == 7:
        for c in cards:
            if c.value <= 7:
                return True
    else:
        for c in cards:
            if c.value >= topcard_v:
                return True
    return False

def playable(card, pile):
    playable = can_play([card], pile)
    if not playable:
        display(card.name + " can't play on " + pile[0].name)
        return False
    return True

def choose(cards): # Player choose a card
    display("Pick a card to play.")
    display_cards(cards)
    return get_int_input(0, len(cards)-1)

def swap_choose(cards): # Player choose a card
    display("Pick a card to put in your faceups.")
    display_cards(cards)
    return get_int_input(0, len(cards)-1)

def sort_cards(cards): # Sorts card objects in an iterable by card.value
    return sorted(cards, key=lambda card: card.value)
