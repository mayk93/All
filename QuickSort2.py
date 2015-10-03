import random

def LastElement(A):
    if len(A) <= 0:
        print("Empty array.")
        return None
    return A[len(A)-1]

def RandomElement(A):
    randomElementIndex = random.randrange(0,len(A))
    A[randomElementIndex],A[len(A)-1]=A[len(A)-1],A[randomElementIndex]
    return A[len(A)-1]

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

def QuickSortRoutine(A,start,end,choosePivot=LastElement):
    if start < end:
        pivotIndex = Partition(A,start,end)
        QuickSortRoutine(A,start,pivotIndex-1)
        QuickSortRoutine(A,pivotIndex+1,end)

def QuickSort(A,choosePivot=LastElement):
    QuickSortRoutine(A,0,len(A)-1)

A = [5,2,10,7,4,1,9,6,8,3]
QuickSort(A,choosePivot=RandomElement)
print(A)
