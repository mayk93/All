import time
import copy

class Heap():
    def __init__(self,array=[]):
        self.array = array
        self.length = len(array)
        self.heapSize = len(array)
    def __str__(self):
        tree = self.Tree()
        return ('---\n'+'Heap:\n'+str(self.array)+'\nArray Length: '+str(self.length)+'\nHeap Size: '+str(self.heapSize)+'\nTree:\n'+tree+'\n---\n')
    def Tree(self):
        tree = ""
        for (index,element) in enumerate(self.array):
            tree += "Children of " + str(element) + " on position " + str(index) + " are: " + (str(self.array[Left(index)]) if Left(index) < self.heapSize else "NIL") + " and " + (str(self.array[Right(index)]) if Right(index) < self.heapSize else "NIL") + "\n"
        return tree

def Left(i):
    return 2*i+1
def Right(i):
    return 2*i+2
def Parent(i):
    if i == 0 or 1:
        return 0
    return i/2-1
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
# Max Heapify Implementations
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
    if left < newHeap.heapSize and newHeap.array[left] > newHeap.array[i]:
        largest = left
    if right < newHeap.heapSize and newHeap.array[right] > newHeap.array[largest]:
        largest = right
    if largest != i:
        newHeap.array[i],newHeap.array[largest] = newHeap.array[largest],newHeap.array[i]
        MaxHeapifyRecursiveInplace(newHeap,largest)
    return newHeap

def MaxHeapifyIterativeInplace(H,i):
    if H.length <= 0:
        print("This heap is empty.")
        return
    if H.length == 1:
        return
    while True:
        left = Left(i)
        right = Right(i)
        largest = i
        if left < H.heapSize and H.array[left] > H.array[i]:
            largest = left
        if right < H.heapSize and H.array[right] > H.array[largest]:
            largest = right
        if i == largest:
            return
        else:
            H.array[i],H.array[largest] = H.array[largest],H.array[i]
        i = largest

def MaxHeapifyIterativeNewHeap(H,i):
    if H.length <= 0:
        print("This heap is empty.")
        return copy.deepcopy(H)
    if H.length == 1:
        return copy.deepcopy(H)
    newHeap = copy.deepcopy(H)
    while True:
        left = Left(i)
        right = Right(i)
        largest = i
        if left < newHeap.heapSize and newHeap.array[left] > newHeap.array[i]:
            largest = left
        if right < newHeap.heapSize and newHeap.array[right] > newHeap.array[largest]:
            largest = right
        if i == largest:
            return newHeap
        else:
            newHeap.array[i],newHeap.array[largest] = newHeap.array[largest],newHeap.array[i]
        i = largest

# Min Heapify Implementations
def MinHeapifyRecursiveInplace(H,i):
    if H.length <= 0:
        print('This heap is empty.')
        return
    if H.length == 1:
        return
    left = Left(i)
    right = Right(i)
    smallest = i
    if left < H.heapSize and H.array[left] < H.array[i]:
        smallest = left
    if right < H.heapSize and H.array[right] < H.array[smallest]:
        smallest = right
    if smallest != i:
        H.array[i],H.array[smallest] = H.array[smallest],H.array[i]
        MinHeapifyRecursiveInplace(H,smallest)

def MinHeapifyRecursiveNewHeap(H,i):
    if H.length <= 0:
        print('This heap is empty.')
        return copy.deepcopy(H)
    if H.length == 1:
        return copy.deepcopy(H)
    left = Left(i)
    right = Right(i)
    smallest = i
    newHeap = copy.deepcopy(H)
    if left < newHeap.heapSize and newHeap.array[left] < newHeap.array[i]:
        smallest = left
    if right < newHeap.heapSize and newHeap.array[right] < newHeap.array[smallest]:
        smallest = right
    if smallest != i:
        newHeap.array[i],newHeap.array[smallest] = newHeap.array[smallest],newHeap.array[i]
        MinHeapifyRecursiveInplace(newHeap,smallest)
    return newHeap

def BuildHeap(H):
    for (index,element) in enumerate(reversed(H.array[(H.length)/2:])):
        index = H.length/2-index
        MinHeapifyRecursiveInplace(H,index)

def GetHeap(H):
    newHeap = copy.deepcopy(H)
    for (index,element) in enumerate(reversed(newHeap.array[(newHeap.length)/2:])):
        index = newHeap.length/2-index
        MinHeapifyRecursiveInplace(newHeap,index)
    return newHeap

A = [16,4,10,14,7,9,3,2,8,1]
B = [1,100,3,17,19,36,7,25,2]
C = [0,100,5,1,7,4,3,8]
H = Heap(array=C)