from datetime import datetime, date, time

def Swap(array,index1,index2):
    aux = array[index1]
    array[index1] = array[index2]
    array[index2] = aux

def Partition(array,start,end):
    pivot = array[end]
    newPivotIndex = start - 1 #Yes, outside the array
    for arrayIndex in range(start,end):
        if array[arrayIndex] < pivot:
            newPivotIndex += 1
            Swap(array,newPivotIndex,arrayIndex)
    Swap(array,newPivotIndex+1,end)
    return newPivotIndex+1

def QuickSortAux(array,start,end):
    if start < end:
        pivotIndex = Partition(array,start,end)
        QuickSortAux(array,start,pivotIndex-1)
        QuickSortAux(array,pivotIndex+1,end)

def QuickSort(array):
    QuickSortAux(array,0,len(array)-1)

array = [2,1,8,3,7,9,10,5,4,6,0]
print("Initial array: " + str(array))
start = datetime.now()
QuickSort(array)
end = datetime.now()
print("Sorted Array: " + str(array))
print("Execution Time: " + str(end-start))
