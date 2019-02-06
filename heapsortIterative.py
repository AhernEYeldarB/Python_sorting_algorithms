# Bradley Aherne, 117340053
'''
    Implementation of an in-place (Using the existing structure) Heapsort algorithm for a Min Heap.

    Must also create a test case for the algorithm 

    Try implement bubbling down and not up !

    Complexity:
        Add := O( log n )
        Remove := O( log n )
        Search := O( 1 )
'''
from math import ceil


# find left right and parent nodes respectively retunrs theur index
def left(index):
    return (2 * index) + 1


def _buildIter(array, index, end):
    largest = left(index)
    while largest < end:
        if (largest < end) and (array[largest] < array[largest + 1]):
            largest += 1

        if array[largest] > array[index]:
            array[largest], array[index] = array[index], array[largest]
            index = largest
        else:
            return


# def buildIter(array):
#     end = len(array)
#     for i in reversed((range(ceil(end / 2)))):
#         _buildIter(array, i, end)
#     return array


def heapsort(array):
    
    def _buildIter(index, end):
        largest = left(index)
        while left(index) <= end:
            largest = left(index)
            if (largest < end) and (array[largest] < array[largest + 1]):
                largest += 1

            if array[largest] > array[index]:
                array[largest], array[index] = array[index], array[largest]
                index = largest
            else:
                return

    end = len(array) - 1
    virtualLength = ceil(len(array)//2)

    while virtualLength >= 0:
        _buildIter(virtualLength, end)
        virtualLength -= 1

    while end > 0:
        array[0], array[end] = array[end], array[0]
        end -= 1 
        _buildIter(0, end)
        
    return array