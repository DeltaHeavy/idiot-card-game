from Interface import *

def get_input(message=None):
    if message:
        display(message)
    return input()

def get_int_input(low, high):
    choice = None
    while choice is None:
        try:
            choice = int(get_input())
            if choice not in range(low, high+1):
                raise ValueError
        except:
            display("Invalid input. Enter a number from " + low + " to " + high + ".")
            choice = None
    return choice

def get_player_counts():
    display("How many human players? [0-5]")
    human_pcount = get_int_input(0, 5)
    display("How many cpu players?")
    cpu_pcount = get_int_input(2-human_pcount if human_pcount < 2 else 0, 5-human_pcount)
    return human_pcount, cpu_pcount

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

def choose(cards):
    display_cards(cards)
    return get_int_input(0, len(cards))

def sort_cards(cards):
    return sorted(cards, key=lambda card: card.value)

def victory(player):
    display(player.name + "is the winner!")
