from GameEngine_Functions import *

def isnextnextwinning(handlen, fdcount):
    if handlen is None:
        return None
    if handlen > 0:
        return False
    elif fdcount > 1:
        return False
    return True

class OP: # An AI's opponent
    def __init__(self): # Only things a player would know about their opponents
        self.handcount = 3
        self.faceups = []
        self.fdcount = 3
        self.nextnextwinning = False

class AI: # The AI itself
    def __init__(self, name):
        self.name = name # It's own player's name
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
        self.nextnextwinning = isnextnextwinning(info[7], info[8])

    def cpu_choose(self):
        raise NotImplementedError
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
        # 0. Check for op about to win
        # 1. Check for nextnextwinning if nextnextwinning is not None
        # 2. Check for completion of 4-of-a-kind
        # 3. Check for op can't play faceups
        # 4. Play 6 on 7 if 7 in hand
        # 5. Play lowest playable
