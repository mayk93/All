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

universeLimit = 5
UNIVERSE = generateUniverse()
multisetT = generatemultisetT(UNIVERSE , 5)

""" Ranking class """
class ranking:
    def __init__(self):
        self.rankedList = []
    def populateRankedList(self):
        self.rankedList = random.sample(range(50), 5)
        self.rankedList.sort()
        self.rankedList.reverse()
    def getRank(self,x):
        for i in range (0,len(self.rankedList)-1):
            if x == self.rankedList[i]:
                return i + 1
        return len(self.rankedList) + 1
    def checkIfFullRanking (self):
        self.rankList()
        if self.orderedRankedList == UNIVERSE:
            return True
        else:
            return False

""" Metrics """
def SpearmanFootRuleDistance ( sigma, tau ):

    """
    [0, 2, 4, 3, 1]
    [3, 4, 2, 0, 1]
    0

    De ce?
    """
    
    distance = 0

    print(sigma.rankedList)
    print(tau.rankedList)
    
    for i in UNIVERSE:
        """ Print for debugging purposes """
        if i in sigma.rankedList:
            print("Found ", i," in SIGMA. It has rank " , sigma.getRank(i),".")
        if i in tau.rankedList:
            print("Found ", i," in TAU. It has rank ", tau.getRank(i),".")
        if i in sigma.rankedList or i in tau.rankedList:
            print("Current distance is ", distance ,".")
        
        distance = distance + abs(sigma.getRank(i) - tau.getRank(i))
        
        if i in sigma.rankedList or i in tau.rankedList:
            print("Computed abs is ", abs(sigma.getRank(i) - tau.getRank(i)) ,".")
            print("New distance is ", distance,".")
        
    return distance

    """
    [0, 1, 2, 3, 4]
    [3, 2, 1, 0, 4]
    Found  2  in TAU. It has rank  6 .
    Current distance is  0 .
    Computed abs is  0 .
    New distance is  0 .
    Found  0  in SIGMA. It has rank  6 .
    Current distance is  0 .
    Computed abs is  0 .
    New distance is  0 .
    0

    WTF? De ce nu apare 2 in SIGMA?
    """

def  KendallTauDistance ( sigma, tau ):
    return 0

""" Ord """
def ord ( sigma , x ):
    print(len(sigma.rankedList)+1)
    print(sigma.getRank(x))
    return abs((len(sigma.rankedList)+1)-sigma.getRank(x))
    
def main ():
    sigma = ranking()
    #sigma.populateRankedList()

    tau = ranking()
    #tau.populateRankedList()

    
    sigma.rankedList = [0,3,1,4,2]
    print(sigma.rankedList)
    tau.rankedList = [4,2,1,3,0]
    print(tau.rankedList)
    print(SpearmanFootRuleDistance(sigma,tau))
    
    
if __name__ == "__main__":
    main()
