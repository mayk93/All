verbose = False

def Pairs(A):
    for i in range(0,len(A),2):
        yield A[i:i+2]

def FindSecondSmallest(A,formerLoosers,lostTo):

    if verbose:
        print("---")
        print("Was called with: ")
        print("A: "+str(A))
        print("Former Loosers: "+str(formerLoosers))

    if len(A) == 1:
        numbersThatLostToCurrentWinner = lostTo[A[0]]
        print("Lost to: "+str(lostTo))
        return min(numbersThatLostToCurrentWinner)
        #return A[0] #This is the minimum

    pairs = list(Pairs(A))
    winners = []
    loosers = []
    for pair in pairs:
        currentWinner = min(pair)
        currentLooser = max(pair)
        winners.append(currentWinner)
        loosers.append(currentLooser)

        numbersThatLostToCurrentWinner = []
        try:
            numbersThatLostToCurrentWinner = lostTo[currentWinner]
        except:
            numbersThatLostToCurrentWinner.append(currentLooser)
            lostTo.update({currentWinner:numbersThatLostToCurrentWinner})
        numbersThatLostToCurrentWinner.append(currentLooser)
        lostTo.update({currentWinner:numbersThatLostToCurrentWinner})

    if verbose:
        print("Calling with: ")
        print("Winners (A): "+str(winners))
        print("Loosers: "+str(loosers))
        print("---")

    minimum = FindSecondSmallest(winners,loosers,lostTo)
    return minimum

y = FindSecondSmallest([0,2,3,4,-1,5,7],[],{})
print(y)
