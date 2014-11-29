class OP: # An AI's opponent
    def __init__(self): # Only things a player would know about their opponents
        self.handcount = 0
        self.faceups = []
        self.fdcount = 0

class AI: # The AI itself
    def __init__(self, name, pcount):
        self.name = name # It's own player's name
        self.decklength = 0 # Initial values
        self.pile = []
        self.ops = [] # A list of opponents
        for i in range(pcount-1):
            self.ops.append(OP())

    def update(self, info): # Takes info about game state from the Game class
        self.decklength = info.pop(0)
        self.pile = info.pop(0)
        for l in info:
            if l[0] == self.name: # Mr. AI, don't count yourself as an opponent
                info.remove(l)
        for i in range(len(self.ops)): # Update information about opponents
            self.ops[i].handcount = info[i][1]
            self.ops[i].faceups = info[i][2]
            self.ops[i].fdcount = info[i][3]

    def cpu_choose(self):
        raise NotImplementedError
