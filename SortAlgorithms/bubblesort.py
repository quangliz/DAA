import random
def bubbleSort(array):
    indexOfLastUnsortedElement = len(array)
    for i in range(len(array)):
        swap = False
        for j in range(indexOfLastUnsortedElement - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if swap == False: break
        indexOfLastUnsortedElement -= 1 # reduce last unsorted elements
arr = [random.randint(0, 100) for _ in range(20)]
print(arr)
bubbleSort(arr)
for i in range(len(arr)):
    print(arr[i], end = " ")