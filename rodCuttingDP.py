from datetime import datetime, date, time

'''
Vanilla rod cutting (cuts are free)
'''

'''
Build dictionary
'''
pricePerLength = {0:0} #length : price
lengths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

for length,price in zip(lengths,prices):
    pricePerLength.update({length:price})

'''
Exponential
'''

def GetOptimalRevenueExponential(lengthOfRod):
    if lengthOfRod == 0:
        return pricePerLength[lengthOfRod]
    else:
        possibilities = [ ( pricePerLength[lengthToCut] + GetOptimalRevenueExponential(lengthOfRod-lengthToCut) ) for lengthToCut in range(1,lengthOfRod+1) ]
        return max(possibilities)

start = datetime.now()
print("Expondential: " + str(GetOptimalRevenueExponential(7)))
end = datetime.now()
print("Exponential executed in: " + str(end-start))

'''
Top Down - Memoization
'''

def GetOptimalRevenueTopDownAux(lengthOfRod,revenue):
    if revenue[lengthOfRod] >= 0:
        return revenue[lengthOfRod]
    elif lengthOfRod == 0:
        revenue.update({0:0})
        return 0
    else:
        possibilities = [ ( pricePerLength[lengthToCut] + GetOptimalRevenueTopDownAux(lengthOfRod-lengthToCut,revenue) ) for lengthToCut in range(1,lengthOfRod+1)]
        revenue[lengthOfRod] = max(possibilities)
        return revenue[lengthOfRod]

def GetOptimalRevenueTopDown(lengthOfRod):
    revenue = { length:-1 for length in range(lengthOfRod+1)  }
    return GetOptimalRevenueTopDownAux(lengthOfRod,revenue)

start = datetime.now()
print("Top Down: " + str(GetOptimalRevenueTopDown(7)))
end = datetime.now()
print("Top down executed in: " + str(end-start))

'''
Bottom Up
'''

def GetOptimalRevenueBottomUp(lengthOfRod):
    revenue = {length:-1 for length in range(lengthOfRod+1)}
    revenue[0] = 0
    for lengthToCut1 in range(1,lengthOfRod+1):
        possibilities = [ ( pricePerLength[lengthToCut2] + revenue[lengthToCut1-lengthToCut2] ) for lengthToCut2 in range(1,lengthToCut1+1) ]
        revenue[lengthToCut1] = max(possibilities)
    return revenue[lengthOfRod]

start = datetime.now()
print("Bottom Up: " + str(GetOptimalRevenueBottomUp(7)))
end = datetime.now()
print("Bottom Up executed in: " + str(end-start))

'''
Non Vanilla ( Cuts cost )
'''

cutCost = 1

'''
Exponential Cuts
'''

def GetOptimalRevenueExponentialCuts(lengthOfRod):
    if lengthOfRod == 0:
        return pricePerLength[lengthOfRod]
    else:
        possibilities = [ ( pricePerLength[lengthToCut] + GetOptimalRevenueExponentialCuts(lengthOfRod-lengthToCut) - (cutCost*(0 if (lengthOfRod-lengthToCut) == 0 else 1)) ) for lengthToCut in range(1,lengthOfRod+1) ]
        return max(possibilities)

start = datetime.now()
print("Expondential Cuts: " + str(GetOptimalRevenueExponentialCuts(7)))
end = datetime.now()
print("Exponential Cuts executed in: " + str(end-start))

'''
Top Down - Memoization Cuts
'''

def GetOptimalRevenueTopDownAuxCuts(lengthOfRod,revenue):
    if revenue[lengthOfRod] >= 0:
        return revenue[lengthOfRod]
    elif lengthOfRod == 0:
        revenue.update({0:0})
        return 0
    else:
        possibilities = [ ( pricePerLength[lengthToCut] + GetOptimalRevenueTopDownAuxCuts(lengthOfRod-lengthToCut,revenue) - (cutCost*(0 if (lengthOfRod-lengthToCut) == 0 else 1))) for lengthToCut in range(1,lengthOfRod+1)]
        revenue[lengthOfRod] = max(possibilities)
        return revenue[lengthOfRod]

def GetOptimalRevenueTopDownCuts(lengthOfRod):
    revenue = { length:-1 for length in range(lengthOfRod+1)  }
    return GetOptimalRevenueTopDownAuxCuts(lengthOfRod,revenue)

start = datetime.now()
print("Top Down Cuts: " + str(GetOptimalRevenueTopDownCuts(7)))
end = datetime.now()
print("Top down Cuts executed in: " + str(end-start))

'''
Bottom Up Cuts
'''

def GetOptimalRevenueBottomUpCuts(lengthOfRod):
    revenue = {length:-1 for length in range(lengthOfRod+1)}
    revenue[0] = 0
    for lengthToCut1 in range(1,lengthOfRod+1):
        possibilities = [ ( pricePerLength[lengthToCut2] + revenue[lengthToCut1-lengthToCut2] - (cutCost*(0 if (lengthOfRod-lengthToCut2) == 0 else 1)) ) for lengthToCut2 in range(1,lengthToCut1+1) ]
        revenue[lengthToCut1] = max(possibilities)
    return revenue[lengthOfRod]

start = datetime.now()
print("Bottom Up Cuts: " + str(GetOptimalRevenueBottomUpCuts(7)))
end = datetime.now()
print("Bottom Up Cuts executed in: " + str(end-start))
