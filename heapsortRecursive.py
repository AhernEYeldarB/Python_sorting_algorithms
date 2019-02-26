from math import ceil

def _buildRecursive(array, index, end):
    if (2*index)+1 > end-1:
        return
    largest = 2 * index +1

    if (largest < end-1) and (array[largest] < array[largest + 1]):
        largest += 1

    if (array[largest] > array[index]):
        array[largest], array[index] = array[index], array[largest]
        _buildRecursive(array, largest, end-1)
    


def heapsort(array):
    # Recursively Build heap

    end = len(array)
    virtualLength = (len(array) // 2)

    # for i in reversed((range(virtualLength))):
    #     _buildRecursive(array, i, end)

    while virtualLength >= 0:
        _buildRecursive(array, virtualLength, end)
        virtualLength -= 1

    while end > 0:
        array[0], array[end-1] = array[end-1], array[0]
        _buildRecursive(array, 0, end-1)
        end -= 1

    return array