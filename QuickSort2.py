import random

def InsertionSort(A,start,end):
    for (currentIndex,element) in enumerate(A[start+1:end]):
        currentIndex += start+1
        key = A[currentIndex]
        comparisonIndex = currentIndex - 1
        while comparisonIndex >= 0 and A[comparisonIndex] > key:
            A[comparisonIndex+1] = A[comparisonIndex]
            comparisonIndex -= 1
        A[comparisonIndex+1] = key

def FirstElement(A,start,end):
    if len(A) <= 0:
        print("Empty array.")
        return None
    if start < 0 or start >= len(A):
        print("Bad start")
        return None
    return A[start]

def LastElement(A,start,end):
    if len(A) <= 0:
        print("Empty array.")
        return None
    if end < 0 or end > len(A):
        print("Bad end.")
        return None
    return A[end-1]

def RandomElement(A,start,end):
    randomElementIndex = random.randrange(start,end)
    A[randomElementIndex],A[end-1]=A[end-1],A[randomElementIndex]
    return A[end-1]

def MedianElement(A,start,end):
    if len(A) <= 0:
        print("Empty array.")
        return None
    if start < 0 or start >= len(A) or last < 0 or last >= len(A):
        print("Bad start or end.")
        return None
    if start == end:
        return A[start]
    medianCandidates = random.sample(range(start,end), 3)
    InsertionSort(medianCandidates)
    return A[medianCandidates[1]]

def CLRSPartition(A,start,end,choosePivot=LastElement):
    if choosePivot == FirstElement:
        choosePivot = LastElement
    pivot = choosePivot(A,start,end+1)
    boundaryIndex = start - 1
    for (currentIndex,element) in enumerate(A[start:end]):
        currentIndex += start
        if element <= pivot:
            boundaryIndex += 1
            A[boundaryIndex],A[currentIndex] = A[currentIndex],A[boundaryIndex]
    A[boundaryIndex+1],A[end] = A[end],A[boundaryIndex+1]
    return boundaryIndex+1

def HoarePartition(A,start,end,choosePivot=FirstElement):
    pivot = FirstElement(A,start,end+1)
    leftCurrentIndex = start - 1
    rightCurrentIndex = end + 1
    while True:
        while True:
            rightCurrentIndex -= 1
            if A[rightCurrentIndex] <= pivot:
                break
        while True:
            leftCurrentIndex += 1
            if A[leftCurrentIndex] >= pivot:
                break

        if leftCurrentIndex < rightCurrentIndex:
            A[leftCurrentIndex],A[rightCurrentIndex] = A[rightCurrentIndex],A[leftCurrentIndex]
        else:
            return rightCurrentIndex + 1


def QuickSortRoutine(A,start,end,partition=CLRSPartition,choosePivot=LastElement,insertionSortLastKElements=0):
    if start < end:
        if len(A[start:end+1]) <= insertionSortLastKElements:
            InsertionSort(A,start,end+1)
            return
        pivotIndex = partition(A,start,end,choosePivot=choosePivot)
        QuickSortRoutine(A,start,pivotIndex-1,partition=partition,choosePivot=choosePivot,insertionSortLastKElements=insertionSortLastKElements)
        QuickSortRoutine(A,pivotIndex+1,end,partition=partition,choosePivot=choosePivot,insertionSortLastKElements=insertionSortLastKElements)

def QuickSort(A,partition=CLRSPartition,choosePivot=LastElement,insertionSortLastKElements=0):
    QuickSortRoutine(A,0,len(A)-1,partition=partition,choosePivot=choosePivot,insertionSortLastKElements=insertionSortLastKElements)

A = [5,2,10,7,4,1,9,6,8,3,9,2,5,4,4,4,4,4,10,7,0,1]
B = [2,1,3,1,1,1,3,]
C = [1,1,1,1,3,2,3]
QuickSort(A,partition=CLRSPartition,choosePivot=RandomElement,insertionSortLastKElements=0)
print(A)
