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

universeLimit = 7
UNIVERSE = generateUniverse()
multisetT = generatemultisetT(UNIVERSE , 15)

""" Ranking class """
class ranking:
    def __init__(self):
        print("7")
        self.rankedList = []
    def populateRankedList(self,size):
        print("9")
        while len(self.rankedList) < size:
            toAdd = random.choice(UNIVERSE)
            if toAdd in self.rankedList:
                pass
            else:
                self.rankedList.append(toAdd)
    def getRank(self,x):
        for i in range (0,len(self.rankedList)-1):
            if x == self.rankedList[i]:
                return i + 1
        return len(self.rankedList) + 1
    def checkIfFullRanking (self):
        toCheck = list(self.rankedList)
        toCheck.sort()
        if toCheck == UNIVERSE:
            return True
        else:
            return False

""" Metrics """
def SpearmanFootRuleDistance ( sigma, tau ):
    if sigma.checkIfFullRanking() and tau.checkIfFullRanking():  
        distance = 0   
        for i in UNIVERSE:
            """ Print for debugging purposes """
            """
            if i in sigma.rankedList:
                print("Found ", i," in SIGMA. It has rank " , sigma.getRank(i),".")
            if i in tau.rankedList:
                print("Found ", i," in TAU. It has rank ", tau.getRank(i),".")
            if i in sigma.rankedList or i in tau.rankedList:
                print("Current distance is ", distance ,".")
            """
            distance = distance + abs(sigma.getRank(i) - tau.getRank(i))
            """
            if i in sigma.rankedList or i in tau.rankedList:
                print("Computed abs is ", abs(sigma.getRank(i) - tau.getRank(i)) ,".")
                print("New distance is ", distance,".")
            """
        return distance
    else:
        return -1

def KendallTauDistance ( sigma, tau ):
    if sigma.checkIfFullRanking() and tau.checkIfFullRanking(): 
        distance = 0
        """ i and j refer to element of the ranked lists? They are not indices, are they? """
        for i, j in zip(sigma.rankedList, tau.rankedList):
            """ Here i and j are numbers. The comparison should be a given criterion, right? """
            if i < j and sigma.getRank(i) < sigma.getRank(j) and tau.getRank(i) > tau.getRank(j):
                distance = distance + 1
        return distance
    else:
        return -1
                

def RankedDistance ( sigma, tau ):
    """
    On full rankedLists it does yield the same result as the Spearman distance, which is good.
    However, I am still unsure it is correct.
    """
    distance = 0
    """ Remove duplicates, yes? """
    biglist = []
    biglist[:] = unique( sigma.rankedList + tau.rankedList )
    """ Print for debugging purposes """
    """
    print(sigma.rankedList)
    print(tau.rankedList)
    print(biglist)
    """
    for x in biglist:
        distance = distance + abs(ord(sigma,x) - ord(tau,x))
    return distance
    
""" Ord """
def ord ( sigma , x ):
    print("12")
    return abs((len(sigma.rankedList)+1)-sigma.getRank(x))

""" Auxiliary methods """
def unique( seq ):
    seen = set()
    for item in seq:
        if item not in seen:
            seen.add( item )
            yield item

def constructD (t,k,j):
    print("5")
    toReturn = 0
    #print("In construct D, t =",t)
    #print("In construct D, j =",j)
    for i in range (1,j+1):
        print("6")
        #print("In construct D, i =",i," out of",j)
        tauI = ranking()
        print("8")
        #tauI.populateRankedList(len(multisetT[i]))
        print("10")
        #print(tauI.rankedList)
        tauI.rankedList = list(multisetT[i])
        print("11")
        #print(tauI.rankedList)
        if j <= t:
            print("11.0")
            #print(j,"<=",t)
            toReturn = toReturn + abs(j-ord(tauI,k))
            #print("Done if")
        else:
            print("11.1")
            #print(j,">",t)
            toReturn = toReturn + abs(ord(tauI,k))
            #print("Done else")
    print("13")
    return toReturn
        
def computeTAggregation ( t ):
    return 0    

def rankAggregation ():
    print("1")
    D = []
    k = len(multisetT)
    PiTAggregations = []
    print("2")
    for t in range(1,len(UNIVERSE)+1):
        print("3")
        toAppendToD = []
        for j in range(1,len(UNIVERSE)+1):
            print("4")
            #print("In rankAggregation, t =",t,"out of",len(UNIVERSE))
            #print("In rankAggregation, j =",j,"out of",len(UNIVERSE))
            toAppend = constructD(t,k,j)
            print("14")
            toAppendToD.append( toAppend )
            print("15")
            #print("In rankAggregation, appended",toAppend )
        #print("To append for t = ",t,":",toAppend)
        print("16")
        D.append(toAppendToD)
        print("17")
    print("18")    
    return D
            #PiTAggregations.append( computeTAggregation(t) )
    
def main ():
    #sigma = ranking()
    #sigma.populateRankedList(3)

    #tau = ranking()
    #tau.populateRankedList(5)

    """
    print(sigma.rankedList)
    print(tau.rankedList)
    print(SpearmanFootRuleDistance(sigma,tau))
    print(KendallTauDistance(sigma,tau)
    print(RankedDistance(sigma,tau))
    """
    print("0")
    print(rankAggregation())
    print("19")
    
if __name__ == "__main__":
    main()
