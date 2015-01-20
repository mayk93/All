""" Libs """
import random

""" Initialization """
def generateUniverse ():
    universe = []
    for i in range (0,universeLimit):
        universe.append(i)
    return universe

def generatemultisetT ( universe , numberOfSets ):
    multiset = []
    for i in range (0,numberOfSets):
        currentSet = []
        for j in range(0,random.randint(5, 10)):
            currentSet.append(random.choice(universe))
        multiset.append(currentSet)
    return multiset

universeLimit = 10
UNIVERSE = generateUniverse()
multisetT = generatemultisetT(UNIVERSE , 10)

""" Ranking class """
class ranking:
    def __init__(self):
        self.rankedList = []
    def populateRankedList(self):
        self.rankedList = random.sample(range(50), 5)
    def rankList(self):
        self.orderedRankedList = self.rankedList
        self.orderedRankedList.sort()
    def getRank(self,x):
        for i in range (0,len(self.rankedList)-1):
            if x == self.rankedList[i]:
                return i
        return len(self.rankedList)
    def checkIfFullRanking (self):
        self.rankList()
        if self.orderedRankedList == UNIVERSE:
            return True
        else:
            return False

""" Metrics """


""" Ord """
def ord ( sigma , x ):
    return abs(len(sigma.rankedList)-sigma.getRank(x))
    
def main ():
    sigma = ranking()
    sigma.populateRankedList()

    tau = ranking()
    tau.populateRankedList()
    
    print(ord(sigma,345))
    print(ord(sigma,sigma.rankedList[3]))
    
if __name__ == "__main__":
    main()
