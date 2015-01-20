Universe = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

multisetT = [  ]

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

def main ():
    print( SpearmanFootRuleDistance( [1,2,3] , [1,3,2] ) )
    print( KendallTauDistance( [1,2,3,4,7,5,6,11,8] , [1,3,2,11,6,5,8,7,4] ) )

if __name__ == "__main__":
    main()
    
