from random import randint
from insertionsort import insertSort

# Possibly check the average smaple median method


def _partition(array, start, end):
    '''
        Function to calculate the partition in a quicksort 
        (Should be pseudorandomly generated and not liner for best expected performance)
    '''
    # Random Pivot implementation
    # if (end-start) < 5:
    #     # print(array[start:end])
    #     print(array)
    #     insertSort(array,start,end)
    #     return end

    randomPivot = randint(start, end)
    array[randomPivot], array[start] = array[start], array[randomPivot]

    pivot = start
    temp = array[start]

    # newPiv = array[pivot]
    for i in range(start + 1, end + 1):
        if array[i] <= temp:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]

    array[pivot], array[start] = array[start], array[pivot]

    return pivot


'''
    Attempt at optimisation 2
'''


def ___quicksort(array, start, end):
    while start < end:
        pivot = _partition(array, start, end)
        if (pivot - start) < (end - pivot):
            ___quicksort(array, start, pivot - 1)

            start = pivot + 1
        else:
            ___quicksort(array, pivot + 1, end)
            end = pivot - 1
    return array, start, end


'''
    Original Function
'''

# def _quicksort(array, start=0, end=None):
#     if end == None:
#         end = len(array) - 1

#     if start >= end:
#         return

#     pivot = _partition(array, start, end)

#     _quicksort(array, start, pivot - 1)

#     _quicksort(array, pivot + 1, end)

#     return array, start, end
'''
    Attempt at optimisation 1
'''

# def __quicksort(array, start, end):
#     while start < end:

#         pivot = _partition(array, start, end)

#         __quicksort(array, start, pivot - 1)

#         start = pivot + 1

#     return array, start, end


def quicksort(array):
    end = len(array) - 1
    return ___quicksort(array, 0, end)[0]


# if __name__ == "__main__":
#     '''
#         Will implement a benchmark
#     '''

#     def main():
#         pass

# main()
