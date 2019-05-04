# Implementation of In-Place Quickselect algorithm to find nth smallest element in an unordered list
from random import randint

# Possibly check the average smaple median method
# Can start first check with the given index in the case its already sorted

def _partition(array, start, end):
    '''
        Function to calculate the partition in a quickselect 
    '''
    # Select a random pivot in the list
    randomPivot = randint(start, end)
    array[randomPivot], array[start] = array[start], array[randomPivot]

    # Swap pivot with index 0
    pivot = start
    temp = array[start]

    # Put elements less than pivot to left, elements greater than pivot to right of pivot
    for i in range(start + 1, end + 1):
        if array[i] <= temp:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]

    array[pivot], array[start] = array[start], array[pivot]

    return pivot



def _quickselect(array, start, end, index):
    # Continue sorting until you find the element at given index index
    while start <= end:
        pivot = _partition(array, start, end)
        
        if pivot == index:
            return array[pivot]

        if pivot > index:
            element = _quickselect(array, start, pivot - 1, index)
            start = pivot + 1

        else:
            element = _quickselect(array, pivot + 1, end, index)
            end = pivot - 1
        
        return element


def quickselect(array, index):
    end = len(array) - 1
    return _quickselect(array, 0 ,end, index)

if __name__ == "__main__":
    newList = [6,3,2,7,1,8,20]
    index = 2
    element = quickselect(newList,index)
    print(index, element)