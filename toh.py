class Disc:
    def __init__(self, val):
        self.value = val

    def getDiscValue(self):
        return '(' + str(self.value) + ')'


class Tower:
    def __init__(self, nm):
        self.name = nm
        self.rod = []

    def getName(self):
        return self.name

    def addDisc(self, objDisc):
        self.rod.append(objDisc) # add at end

    def removeDisc(self):
        if len(self.rod) >0:
            return self.rod.pop(-1) #remove from end
        return None

    def length(self):
        return len(self.rod)

    def getDiscAtPosition(self, pos):
        if pos >= len(self.rod):
            return '| |'
        else:
            return self.rod[pos].getDiscValue()

#GAME
class TowersOfHanoi:
    def __init__(self, x=3 ):
        self.no_of_discs = x

        #creating three towers
        self.source = Tower('A')
        self.target = Tower('B')
        self.aux = Tower('C')

        #adding x discs to source tower
        for i in range(x,0, -1):
            self.source.addDisc(Disc(i))

    def displayAllTowers(self):
        m = max(self.source.length(), self.target.length(), self.aux.length())
        for i in range(m,-1, -1):#3,2,1,0
            print(self.source.getDiscAtPosition(i), self.target.getDiscAtPosition(i), self.aux.getDiscAtPosition(i), sep='\t\t')
        print('='+self.source.getName()+'=', '='+self.target.getName()+'=', '='+self.aux.getName()+'=', sep='\t\t')


    def md(self, n, src, trg, aux):
        if n >0:
            self.md(n-1, src, aux, trg) #moving n-1 discs from src to aux
            trg.addDisc(src.removeDisc()) #moving nth disc from src to trg
            self.displayAllTowers()
            self.md(n-1, aux, trg, src) #moving n-1 discs from aux to trg

    def move_discs(self):
        self.md(self.no_of_discs, self.source, self.target, self.aux)

def main():
    toh = TowersOfHanoi(3)
    toh.displayAllTowers()
    toh.move_discs()

main()

