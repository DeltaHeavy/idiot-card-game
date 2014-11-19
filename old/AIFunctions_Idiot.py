def autoplay_from_hand(hand, pile): # At this point, playable(hand, pile) == True
    chosen = [] # Cards to be played
    values = [card.value for card in hand]  # Values of cards in hand
    top_card = pile.cards[len(pile.cards)-1]
    if completes_four(values, pile): # If we can play into a four of a kind
        for card in hand:
            if card.value == top_card.value:
                chosen.append(card)
        for x in range(len(chosen)):
            hand.remove(chosen[x])
        return chosen # Do it
    for i in range(len(values)): # In order to make min(values) ignore twos and tens,
        if values[i] == 2:
            values[i] = 22 # Twos become 22s
        elif values[i] == 10:
            values[i] = 30 # Tens become 30s
    min_val = min(values)
    if top_card.value == 7: # If 7
        if min_val <= 7: # If we have a low card
            for card in hand:
                if card.value == min_val: # Play all of the lowest card
                    chosen.append(card)
            for x in range(len(chosen)):
                hand.remove(chosen[x])
            return chosen # If we don't have a low card, we must have a two or a ten
        elif 22 in values: # So play one two if we have it
            for card in hand:
                if card.value == 2:
                    chosen.append(card)
                    hand.remove(card)
                    return chosen
        elif 30 in values: # Or one ten if we don't have a two
            for card in hand:
                if card.value == 10:
                    chosen.append(card)
                    hand.remove(card)
                    return chosen
    elif top_card.value in [0, 2]: # Elif empty pile or 2 (i.e. we can play anything)
        if min_val < 22: # If our lowest is a normal card
            for card in hand:
                if card.value == min_val:
                    chosen.append(card)
            for x in range(len(chosen)):
                hand.remove(chosen[x])
            return chosen # Play all copies of it
        elif 22 in values: # If our lowest is 2 or 10
            for card in hand:
                if card.value == 2:
                    chosen.append(card)
                    hand.remove(card)
                    return chosen # Play one 2
        elif 30 in values: # Or a ten, if there aren't twos
            for card in hand:
                if card.value == 10:
                    chosen.append(card)
                    hand.remove(card)
                    return chosen
    else: # Elif normal card
        if min_val >= top_card.value and min_val < 22: # If we can play our lowest
            for card in hand:
                if card.value == min_val:
                    chosen.append(card)
            for x in range(len(chosen)):
                hand.remove(chosen[x])
            return chosen # Do it
        elif min_val < 22: # If we can't play our lowest, but we're still looking at normal cards
            s_v = sorted(list(set(values))) # s_v is our list of unique card values in ascending order
            while not chosen:
                values.remove(values[values.index(s_v[0])]) # Our lowest is too low
                s_v.remove(s_v[0]) # So get rid of it from both places
                next_min_val = s_v[0] # Get the next lowest card
                if next_min_val < 22 and next_min_val >= top_card.value: # If it's playable and normal
                    for card in hand:
                        if card.value == next_min_val: # Add it to chosen
                            chosen.append(card)
                    for x in range(len(chosen)):
                        hand.remove(chosen[x])
                    return chosen # If it's not a 2 or a 10, get all of them before returning
                elif next_min_val == 22: # Elif it's a two
                    for card in hand:
                        if card.value == 2:
                            chosen.append(card)
                            hand.remove(card)
                            return chosen # Play one 2
                elif next_min_val == 30: # Elif it's a 10
                    for card in hand:
                        if card.value == 10:
                            chosen.append(card)
                            hand.remove(card)
                            return chosen # Play one 10
        elif min_val == 22: # If our lowest is a 2
            if len(list(set(values))) == 1 and len(hand) < 3: # If twos are our only cards, and our hand is fewer than three cards, and we haven't drawn (i.e. the deck is gone)
                for card in hand:
                    if card.value == 2:
                        chosen.append(card)
                for x in range(len(chosen)):
                    hand.remove(chosen[x])
                return chosen # Play both 2s
            else: # In any other situation
                for card in hand:
                    if card.value == 2:
                        chosen.append(card)
                        hand.remove(card)
                        return chosen # Play one 2
        elif min_val == 30: # If our lowest is a 10
            for card in hand:
                if card.value == 10:
                    chosen.append(card)
                    hand.remove(card)
                    return chosen # Play one 10

def autoplay_from_faceups(faceups, pile):
    chosen = []
    values = [card.value for card in faceups]
    for i in range(len(values)): # 2 -> 22, 10 -> 30
        if values[i] == 2:
            values[i] = 22
        elif values[i] == 10:
            values[i] = 30
    min_val = min(values) # Get the lowest
    if not playable(faceups, pile): # If the faceups are futile
        for card in faceups:
            if card.value == min_val: # Play the lowest anyway
                chosen.append(card)
        for x in range(len(chosen)):
            faceups.remove(chosen[x])
        return chosen # And then in pile.played() we'll have to pick it all up
    else: # If we can play something
        top_card = pile.cards[len(pile.cards)-1]
        if top_card.value == 7: # Try to play our lowest on a seven
            if min_val <= 7:
                for card in faceups:
                    if card.value == min_val:
                        chosen.append(card)
                for x in range(len(chosen)):
                    faceups.remove(chosen[x])
                return chosen
            elif 22 in values: # Otherwise play our 2s on a seven
                for card in faceups:
                    if card.value == 2:
                        chosen.append(card)
                for x in range(len(chosen)):
                    faceups.remove(chosen[x])
                return chosen
            elif 30 in values: # Otherwise play one 10 on a seven
                for card in faceups:
                    if card.value == 10:
                        chosen.append(card)
                        faceups.remove(card)
                        return chosen
        elif top_card.value in [0, 2]: # If we can play anything we want
            if min_val < 22:
                for card in faceups:
                    if card.value == min_val: # Play all of our lowest
                        chosen.append(card)
                for x in range(len(chosen)):
                    faceups.remove(chosen[x])
                return chosen
            elif min_val == 22: # Or one 2
                for card in faceups:
                    if card.value == 2:
                        chosen.append(card)
                for x in range(len(chosen)):
                    faceups.remove(chosen[x])
                return chosen
            elif min_val == 30: # Or one 10 if we have nothing else
                for card in faceups:
                    if card.value == 10:
                        chosen.append(card)
                        faceups.remove(card)
                        return chosen
        else: # We're playing on a normal card
            if min_val < 22 and min_val >= top_card.value: # If we can play our lowest
                for card in faceups:
                    if card.value == min_val: # Then play all of them
                        chosen.append(card)
                for x in range(len(chosen)):
                    faceups.remove(chosen[x])
                return chosen
            elif min_val < 22: # If our lowest doesn't cut it
                s_v = sorted(list(set(values)))
                while not chosen:
                    if len(s_v) == 1: # If that's our only unique card
                        for card in faceups:
                            chosen.append(card)
                        for x in range(len(chosen)):
                            faceups.remove(chosen[x])
                        return chosen # Play all copies of it
                    values.remove(values[values.index(s_v[0])]) # Our lowest is too low
                    s_v.remove(s_v[0]) # So get rid of it
                    next_min_val = s_v[0]
                    if next_min_val >= top_card.value and next_min_val < 22: # If we can play our next lowest,
                        for card in faceups:
                            if card.value == next_min_val:
                                chosen.append(card)
                        for x in range(len(chosen)):
                            faceups.remove(chosen[x])
                        return chosen # Do it
                    elif next_min_val == 22:
                        for card in faceups:
                            if card.value == 2:
                                chosen.append(card)
                        for x in range(len(chosen)):
                            faceups.remove(chosen[x])
                        return chosen
                    elif next_min_val == 30: # Otherwise if our next lowest is a 10
                        for card in faceups:
                            if card.value == 10:
                                chosen.append(card)
                                faceups.remove(card)
                                return chosen # play one 10
            elif min_val == 22:
                for card in faceups:
                    if card.value == 2:
                        chosen.append(card)
                for x in range(len(chosen)):
                    faceups.remove(chosen[x])
                return chosen
            elif min_val == 30:
                for card in faceups:
                    if card.value == 10:
                        chosen.append(card)
                        faceups.remove(card)
                        return chosen
