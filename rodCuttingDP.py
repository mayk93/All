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
print("Expondential: ", str(GetOptimalRevenueExponential(10)))
end = datetime.now()
print("Exponential executed in: ", str(end-start))

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
print("Top Down: ",str(GetOptimalRevenueTopDown(10)))
end = datetime.now()
print("Top down executed in: ", str(end-start))

'''
Bottom Up
'''
def GetOptimalRevenueBottomUpAux():
    pass

def GetOptimalRevenueBottomUp():
    pass
