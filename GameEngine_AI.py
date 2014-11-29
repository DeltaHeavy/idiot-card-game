class OP:
    def __init__(self):
        self.handcount = 0
        self.faceups = []
        self.fdcount = 0

class AI:
    def __init__(self, name, pcount):
        self.name = name
        self.ops = []
        self.decklength = 0
        self.pile = []
        for i in range(pcount-1):
            self.ops.append(OP())

    def update(self, info):
        self.decklength = info.pop(0)
        self.pile = info.pop(0)
        for l in info:
            if l[0] == self.name:
                info.remove(l[0])
        for i in range(len(self.ops)):
            self.ops[i].handcount = info[i][1]
            self.ops[i].faceups = info[i][2]
            self.ops[i].fdcount = info[i][3]

    def cpu_choose(self):
        raise NotImplementedError
