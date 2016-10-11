monthToNumber = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
numberToMonth = {number:month for month,number in monthToNumber.items()}

class Time():
    def __init__(self,timePeriodAsString):
        if type(timePeriodAsString) != type(self):
            if timePeriodAsString.count(' ') > 1:
                timePeriodAsString = timePeriodAsString.split(' ', 1)[-1]
            self.month, self.year = timePeriodAsString.split(' ')
            self.year = int(self.year)
        else:
            print(timePeriodAsString)
    def __str__(self):
        return ("Month: " + self.month + ", year: " + str(self.year))
    def __sub__(self,other):
        yearPeriod = self.year-other.year
        monthPeriod = monthToNumber[self.month] - monthToNumber[other.month] + 1
        return (12*yearPeriod + monthPeriod)
    def __lt__(self, other):
        if (self.year > other.year):
            return False
        elif (self.year < other.year):
            return True
        elif (monthToNumber[self.month]<monthToNumber[other.month]):
            return True
        return False

    def ___le__(self, other):
        if (self.year > other.year):
            return False
        elif (self.year < other.year):
            return True
        elif (monthToNumber[self.month]<=monthToNumber[other.month]):
            return True
        return False

    def __eq__(self, other):
        return (self.year==other.year)and(monthToNumber[self.month]==monthToNumber[other.month])

    def __ne__(self, other):
        return (self.year!=other.year)or(monthToNumber[self.month]!=monthToNumber[other.month])

    def __gt__(self, other):
        if (self.year > other.year):
            return True
        elif (self.year < other.year):
            return False
        elif (monthToNumber[self.month]<=monthToNumber[other.month]):
            return False
        return True

    def __ge__(self, other):
        if (self.year > other.year):
            return True
        elif (self.year < other.year):
            return False
        elif (monthToNumber[self.month]<monthToNumber[other.month]):
            return False
        return True

def OrderLine(line):
    lineList = line.split(';')
    lineMatrix = [lineListElement.split('-') for lineListElement in lineList]
    timePeriods = [(Time(start.strip('\n')),Time(end.strip('\n'))) for start,end in lineMatrix]
    return (timePeriods)

def ToYears(toConvert):
    return int(toConvert/12)

def main(pathToFile):
    toReturn = []
    fileVar = open(pathToFile)
    for line in fileVar:
        orderedTimeObjectLine = OrderLine(line)
        sortedTimeObjects = sorted(orderedTimeObjectLine, key=lambda tup: tup[0])
        timePeriodInMonths = 0
        index = 0
        print(" --- ")
        for period1Index,period1 in enumerate(sortedTimeObjects):
            if(period1Index >= index):
                realStart1 = period1[0]
                print("Real Start: ",str(realStart1))
                start1 = period1[0]
                end1 = period1[1]
                for period2Index,period2 in enumerate(sortedTimeObjects[index:]):
                    start2 = period2[0]
                    end2 = period2[0]
                    if start2 > start1 and start2 < end1 and end2 > end1:
                        print()
                        start1 = start2
                        end1 = end2
                        index = period2Index
                print(" -> Start: ",str(realStart1))
                print(" -> End: ",str(end1))
                print(" -> TPIM: ",str(timePeriodInMonths))
                timePeriodInMonths += end1-realStart1
        toReturn.append(ToYears(timePeriodInMonths))
    for ret in toReturn:
        print(ret)
    return toReturn

main("x.txt")
'''
s = 'Aug 2013-Mar 2014; Apr 2013-Aug 2013; Jun 2014-Aug 2015; Apr 2003-Nov 2004; Apr 2014-Jan 2015'
orderedTimeObjectLine = OrderLine(s)
print('---===--- 1 ---===---')
for x,y in orderedTimeObjectLine:
    print("   Start: ",str(x))
    print("   End: ",str(y))
    print('---')
print('---===---')
sortedBySecond = sorted(orderedTimeObjectLine, key=lambda tup: tup[1])
print('---===--- 2 ---===---')
for x,y in sortedBySecond:
    print("   Start: ",str(x))
    print("   End: ",str(y))
    print('---')
print('---===---')
'''
