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
def SpearmanFootRuleDistance ( sigma, tau ):
    distance = 0
    if len(sigma.rankedList) == len(tau.rankedList):
        for i,j in sigma.rankedList , tau.rankedList:
            distance = distance + abs(sigma.getRank(i) - tau.getRank(j))
        return distance
    else:
        return -1

def  KendallTauDistance ( sigma, tau ):
    distance = 0
    if len(sigma) == len(tau):
        for i in range(0,len(sigma)-2):
            for j in range(i+1,len(sigma)-1):
                if sigma[i] < sigma[j] and tau[i] > tau[j]:
                    distance = distance + 1
        return distance
    else:
        return -1

def ord ( sigma , x ):
    if x in sigma:
        return abs(len(sigma)-sigma.getRank(x))
    else:
        return 0
def main ():
    sigma = ranking()
    sigma.populateRankedList()

    tau = ranking()
    tau.populateRankedList()
    
    SpearmanFootRuleDistance(sigma,tau)
    
if __name__ == "__main__":
    main()
