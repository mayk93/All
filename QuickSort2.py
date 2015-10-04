import random

def InsertionSort(A):
    for (currentIndex,element) in enumerate(A[1:]):
        currentIndex += 1
        key = A[currentIndex]
        comparisonIndex = currentIndex - 1
        while comparisonIndex >= 0 and A[comparisonIndex] > key:
            A[comparisonIndex+1] = A[comparisonIndex]
            comparisonIndex -= 1
        A[comparisonIndex+1] = key

def LastElement(A):
    if len(A) <= 0:
        print("Empty array.")
        return None
    return A[len(A)-1]

def RandomElement(A):
    randomElementIndex = random.randrange(0,len(A))
    A[randomElementIndex],A[len(A)-1]=A[len(A)-1],A[randomElementIndex]
    return A[len(A)-1]

def MedianElement(A):
    medianCandidates = random.sample(range(len(A)), 3)
    InsertionSort(medianCandidates)
    return A[medianCandidates[1]]

def Partition(A,start,end,choosePivot=LastElement):
    pivot = choosePivot(A[start:end+1])
    boundaryIndex = start - 1
    for (currentIndex,element) in enumerate(A[start:end]):
        currentIndex += start
        if element <= pivot:
            boundaryIndex += 1
            A[boundaryIndex],A[currentIndex] = A[currentIndex],A[boundaryIndex]
    A[boundaryIndex+1],A[end] = A[end],A[boundaryIndex+1]
    return boundaryIndex+1

def QuickSortRoutine(A,start,end,choosePivot=LastElement,insertionSortLastKElements=0):
    if start < end:
        if len(A[start:end+1]) <= insertionSortLastKElements:
            InsertionSort(A[start:end+1])
            return
        pivotIndex = Partition(A,start,end)
        QuickSortRoutine(A,start,pivotIndex-1)
        QuickSortRoutine(A,pivotIndex+1,end)

def QuickSort(A,choosePivot=LastElement,insertionSortLastKElements=0):
    QuickSortRoutine(A,0,len(A)-1)

A = [5,2,10,7,4,1,9,6,8,3]
MedianElement(A)
QuickSort(A,choosePivot=MedianElement,insertionSortLastKElements=3)
print(A)
