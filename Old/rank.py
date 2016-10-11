import random

multisetT = [ random.sample(range(50), 5) , random.sample(range(30), 10) , random.sample(range(100), 7) ,
              random.sample(range(50), 5) , random.sample(range(30), 10) , random.sample(range(100), 7)
            ]

def SpearmanFootRuleDistance ( sigma, tau ):
    distance = 0
    if len(sigma) == len(tau):
        for i in range(0,len(sigma)-1):
            distance = distance + abs(sigma[i] - tau[i])
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
        return abs(len(sigma)-sigma(x))
    else:
        return 0

def main ():
    print( SpearmanFootRuleDistance( multisetT[0] , multisetT[3] ) )
    print( KendallTauDistance( multisetT[1] , multisetT[4] ) )
    print( multisetT )

if __name__ == "__main__":
    main()
    
