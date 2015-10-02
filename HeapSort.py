import time
import copy

class Heap():
    def __init__(self,array=[]):
        self.array = array
        self.length = len(array)
        self.heapSize = len(array)
    def __str__(self):
        return ('---\n'+'Heap:\n'+str(self.array)+'\nArray Length: '+str(self.length)+'\nHeap Size: '+str(self.heapSize)+'\n---\n')

def Left(i):
    return 2*i+1
def Right(i):
    return 2*i+2
# The Swap function is deprecated.
'''
def Swap(A,i,j):
    a = A[i]
    b = A[j]
    A.pop(i)
    A.insert(i,b)
    A.pop(j)
    A.insert(j,a)
'''
'''
We get the indices of the current element's (A[i]) children, using Left and
Right. We compare the value of the current element to that of his children.
If one of the children is learger than the element, that child takes it's place.
We recursively call the function to ensure the Max Heap Propriety is preserved
in case we make a swap.
'''
def MaxHeapifyRecursiveInplace(H,i):
    if H.length <= 0:
        print("This heap is empty. Returned none.")
        return
    if H.length == 1:
        return
    left = Left(i)
    right = Right(i)
    largest = i
    if left < H.heapSize and H.array[left] > H.array[i]:
        largest = left
    if right < H.heapSize and H.array[right] > H.array[largest]:
        largest = right
    if largest != i:
        #Swap(H.array,i,largest)
        H.array[i],H.array[largest] = H.array[largest],H.array[i]
        MaxHeapifyRecursiveInplace(H,largest)

def MaxHeapifyRecursiveNewHeap(H,i):
    if H.length <= 1:
        print("This heap is empty.")
        return copy.deepcopy(H)
    if H.length == 1:
        return copy.deepcopy(H)
    left = Left(i)
    right = Right(i)
    largest = i
    newHeap = copy.deepcopy(H)
    if left < H.heapSize and H.array[left] > H.array[i]:
        largest = left
    if right < H.heapSize and H.array[right] > H.array[largest]:
        largest = right
    if largest != i:
        #Swap(H.array,i,largest)
        newHeap.array[i],newHeap.array[largest] = newHeap.array[largest],newHeap.array[i]
        MaxHeapifyRecursiveInplace(newHeap,largest)
    return newHeap

A = [16,4,10,14,7,9,3,2,8,1]
H = Heap(array=A)
