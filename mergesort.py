'''
    Recursive implementation of a top down mergesort
'''
from insertionsort import insertSort

def merge(array, start, mid, end):
    '''
        Algorithm to merge the sub arrays created from mergesort
    '''
    # if (end - start) < 10:
    #     insertSort(array, start, end+1)
    #     return

    lengthLeft = mid - start + 1
    lengthRight = end - mid
    #Partition the left and right sides

    tempArrLeft = [0] * lengthLeft
    tempArrRight = [0] * lengthRight
    # Initialise temporary arrays for holding values

    for i in range(lengthLeft):
        tempArrLeft[i] = array[start + i]
    for i in range(lengthRight):
        tempArrRight[i] = array[mid + 1 + i]
    # Fill Both temporary arrays

    leftIndex = 0
    rightIndex = 0
    mergedIndex = start
    # Initialise iterators

    while (leftIndex < lengthLeft) and (rightIndex < lengthRight):
        # Determine the correct position of the elemnts from the sub array in the final merged array until one of the sub arrays are empty
        if (tempArrLeft[leftIndex] <= tempArrRight[rightIndex]):
            array[mergedIndex] = tempArrLeft[leftIndex]
            leftIndex += 1

        else:
            array[mergedIndex] = tempArrRight[rightIndex]
            rightIndex += 1

        mergedIndex += 1

    # Append the remaining items from the left and right sub lists respectively
    while (leftIndex < lengthLeft):
        array[mergedIndex] = tempArrLeft[leftIndex]
        mergedIndex += 1
        leftIndex += 1

    while (rightIndex < lengthRight):
        array[mergedIndex] = tempArrRight[rightIndex]
        mergedIndex += 1
        rightIndex += 1


def mergesort(array, start, end):
    if (start < end):
        mid = start + (end - start) // 2
        if mid < 10 :
            insertSort(array,start,end+1)
        mergesort(array, start, mid)
        mergesort(array, mid + 1, end)
        merge(array, start, mid, end)
    # print(array)
    return array


# In Place implementation, super slow!
'''
def merge(array, start, mid, end):
    secondStart = mid +1
    if array[secondStart] >= array[mid]:
        return

    while (start <= mid and secondStart <= end):
        if (array[start] <= array[secondStart]):
            start += 1
        else:
            secondValue = array[secondStart]
            index = secondStart

            while (index != start):
                array[index] = array[index -1]
                index -= 1

            array[start] = secondValue

            start += 1
            mid +=1
            secondStart += 1
'''