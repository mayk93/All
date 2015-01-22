""" Libs """
import random
import itertools

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
universePermutations = list(itertools.permutations(UNIVERSE))
multisetT = generatemultisetT(UNIVERSE , 15)

""" Ranking class """
class ranking:
    def __init__(self):
        self.rankedList = []
    def populateRankedList(self,size):
        """ REOWRK THIS IMMIDIETLY, AWEFUL CODE!!! """
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
            distance = distance + abs(sigma.getRank(i) - tau.getRank(i))
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

    if isinstance(sigma,ranking):
        print(tau.rankedList)
    
    distance = 0
    biglist = []
    if isinstance(sigma,ranking):
        biglist[:] = unique( sigma.rankedList + tau.rankedList ) #Wtf?!
    for x in biglist:
        distance = distance + abs(ord(sigma,x) - ord(tau,x))
    return distance

def RankedDistanceMultiset ( tau , multiset ):
    distance = 0
    for tauI in multiset:
        if isinstance(tau,ranking):
            distance = distance + RankedDistance(tau,tauI)
    return distance
    
""" Ord """
def ord ( sigma , x ):
    return abs((len(sigma.rankedList)+1)-sigma.getRank(x))

""" Auxiliary methods """
def unique( seq ):
    seen = set()
    for item in seq:
        if item not in seen:
            seen.add( item )
            yield item

def constructD (t,k,j):
    toReturn = 0
    for i in range (1,j+1):
        tauI = ranking()
        tauI.rankedList = list(multisetT[i])
        if j <= t:
            toReturn = toReturn + abs(j-ord(tauI,k))
        else:
            toReturn = toReturn + abs(ord(tauI,k))
    return toReturn
        
def computeTAggregation ( t ):
    EArray = []
    for permutation in universePermutations:
        E = 0
        for i in range (0,len(list(permutation))):
            for j in range(0,len(UNIVERSE)):
                if j > t:
                    E = E + constructD(t,i,j)
                else:
                    E = E + constructD(t,i,j)
        EArray.append([E,list(permutation)])
    minE = 9999
    for element in EArray:
        if element[0] < minE:
            minE = element[0]
            toReturn = element[1]
    return toReturn

def generateMultisetTRanking(multisetTparameter):
    toReturn = []
    for tauSet in multisetTparameter:
        toAdd = ranking()
        toAdd.rankedList = list(tauSet)
        toReturn.append(toAdd)
    return toReturn

def rankAggregation ():
    tAggregationTauIArray = []
    minValues = []
    for t in range(1,len(UNIVERSE)):
        tAggregationTauI = computeTAggregation(t) # Returneaza mereu [1,2,3,4,5,6] - minimizeaza E-ul, in sensul ca e 0 in acest caz, dar nu cred ca e bine
        tAggregationTauIArray.append(tAggregationTauI)

        multisetTRanking = list(generateMultisetTRanking(multisetT))
        tAggregationTauIRanking = ranking()
        tAggregationTauIRanking.rankedList = tAggregationTauI
        
        minValues.append([RankedDistanceMultiset(tAggregationTauI,multisetTRanking),t]) # This will not work! multisetT is an array of arrays, it needs to be made into an array of rankings
    minMin = 9999
    minTArray = []
    for element in minValues:
        if element[0] <= minMin:
            minMin = element[0]
            minTArray.append(element[1])

    finalTAggregations = []    
    for minT in minTArray:
        finalTAggregations.append(computeTAggregation(minT))

    return finalTAggregations
        
def generateDMatrices ():
    D = []
    k = len(multisetT)
    PiTAggregations = []
    for t in range(1,len(UNIVERSE)+1):
        toAppendToD = []
        for j in range(1,len(UNIVERSE)+1):
            toAppend = constructD(t,k,j)
            toAppendToD.append( toAppend )
        D.append(toAppendToD)   
    return D
    
def main ():
    """
    sigma = ranking()
    sigma.populateRankedList(3)
    tau = ranking()
    tau.populateRankedList(5)
    print(sigma.rankedList)
    print(tau.rankedList)
    print(SpearmanFootRuleDistance(sigma,tau))
    print(KendallTauDistance(sigma,tau)
    print(RankedDistance(sigma,tau))
    """
    print(rankAggregation())
    #D = generateDMatrices()
    
if __name__ == "__main__":
    main()
