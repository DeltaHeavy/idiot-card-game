def completes_four(values, pile): # AI can determine that it could finish a four of a kind
    top_card = pile.cards[len(pile.cards)-1]
    if not top_card.value in values: # If we don't have one of that card
        return False # Then we're done
    hand_count = 0 # We know there's at least one, but we'll count them from zero
    pile_count = 1 # The top card is one of itself
    for v in values:
        if v == top_card.value:
            hand_count += 1 # Count instances of top_card in hand
    if len(pile.cards) < 4-hand_count: # If the pile isn't large enough
        return False # Then we're done
    if hand_count == 3: # Otherwise if we have all of them in the hand except the one on the pile
        return True # Then we're good
    topcards = pile.cards[-3:len(pile.cards)-1] # Otherwise if there are cards on the pile matching the top_card
    topcards.reverse() # We need to check them descendingly
    for v in [card.value for card in topcards]:
        if v == top_card.value:
            pile_count += 1 # Count them if they appear in order
        else:
            break # Or else if they don't match we're done with consecutives
    if hand_count+pile_count == 4: # If we have enough on the pile and in hand
        return True # Then we're good
    return False # Otherwise we're done
