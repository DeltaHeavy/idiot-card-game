# Interface functions which will inject into the GUI
# TODO Graphics
def display(string):
    print(string)

def display_cards(cards):
    for card in cards:
        print(cards.index(card), card.name)
