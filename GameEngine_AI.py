from GameEngine_Functions import *

def can_complete_four(hand, pile): # AI can determine that it could finish a four of a kind
    if not pile:
        return False
    values = [card.value for card in hand]
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

def iswinning(handcount, fdcount): # AI determines if a player is about to win, to know to play high (if next is winning) or low (if next next is winning)
    if None in [handcount, fdcount]:
        return None # eliminates redundant execution for nonexistent next next player
    return handcount+fdcount < 3 and 0 in [handcount, fdcount]

class OP: # An AI's opponent
    def __init__(self): # Only things a player would know about their opponents
        self.handcount = 3
        self.faceups = []
        self.fdcount = 3
        self.nextnextwinning = False

class AI: # The AI itself
    def __init__(self):
        self.hand = []
        self.faceups = []
        self.decklength = 0 # Initial values
        self.pile = []
        self.op = OP() # The next player

    def update(self, info): # Takes info about the next players from the Game class
        self.hand = info[0]
        self.faceups = info[1]
        self.decklength = info[2]
        self.pile = info[3]
        self.op.handcount = info[4]
        self.op.faceups = info[5]
        self.op.fdcount = info[6]
        self.nextnextwinning = iswinning(info[7], info[8]) # nextnext gets a variable so we can use None to represent a flag that this should stop being updated

    def cpu_choose(self):
        from_hand = False
        if self.hand:
            from_hand = True
        playable = []
        if from_hand:
            for card in self.hand:
                if playable([card], self.pile):
                    playable.append(card)
        else:
            for card in self.faceups:
                if playable([card], self.pile):
                    playable.append(card)
        chosen = []
        # 0. Check for completion of 4-of-a-kind
        if can_complete_four(playable, self.pile):
            for card in playable:
                if card.value == self.pile[0].value:
                    chosen.append(card)
            return chosen
        # 1. Check for playing a 4-of-a-kind
        values = [card.value for card in playable]
        for v in values:
            if values.count(v) == 4:
                for c in playable:
                    if c.value == v:
                        chosen.append(c)
                return chosen
        # 2. Check for op can't play faceups
        if self.op.handcount == 0 and self.op.faceups:
            for i in sorted(values):
                if not i == 10:
                    if not can_play(self.op.faceups, [playable[values.index(i)]]:
                        for c in playable:
                            if c.value == i:
                                chosen.append(c)
                        return chosen
        # 3. Check for op about to win
        if iswinning(self.op.handcount, self.op.fdcount):
            for i in range(14, 10, -1):
                if i in values:
                    for c in playable:
                        if c.value == i:
                            chosen.append(c)
                    return chosen
            elif 7 in values:
                for c in playable:
                    if c.value == 7:
                        chosen.append(c)
                return chosen
            for i in range(9, 2, -1):
                if i in values:
                    for c in playable:
                        if c.value == i:
                            chosen.append(c)
                    return chosen
            elif 2 in values:
                for c in playable:
                    if c.value == 2:
                        chosen.append(c)
                return chosen
            else:
                for c in playable:
                    if c.value == 10:
                        return [c]
        # 4. Check for nextnextwinning if nextnextwinning is not None
        if self.nextnextwinning:
            for i in range(3, 15):
                if not (i == 7 or i == 10) and i in values:
                    for c in playable:
                        if c.value == i:
                            chosen.append(c)
                    return chosen
            elif 7 in values and self.op.handcount == 0 and 7 in [c.value for c in self.op.faceups]:
                for c in playable:
                    if c.value == 7:
                        chosen.append(c)
                return chosen
            elif 2 in values:
                for c in playable:
                    if c.value == 2:
                        chosen.append(c)
                return chosen
            else:
                for c in playable:
                    if c.value == 10:
                        return [c]
        # 5. Play lowest playable
        for i in sorted(values):
            if not (i == 2 or i == 10):
                for c in playable:
                    if c.value == i:
                        chosen.append(c)
                return chosen
            elif 2 in values:
                for c in playable:
                    if c.value == 2:
                        return [c]
            elif 10 in values:
                for c in playable:
                    if c.value == 10:
                        return [c]
