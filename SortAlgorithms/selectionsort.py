import random
def selectionsort(array):
    for i in range(len(array)):
        min = i
        for j in range(i, len(array)):
            if array[j] < array[min]: min = j
        array[i], array[min] = array[min], array[i]
arr = [random.randint(0, 100) for _ in range(10)]
print(arr)
selectionsort(arr)
for i in range(len(arr)):
    print(arr[i], end = " ")