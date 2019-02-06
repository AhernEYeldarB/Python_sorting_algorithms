from math import ceil
'''
    Attempt at optimizations 1
'''
# # import quicksort

# # find left right and parent nodes respectively retunrs theur index
# def left(index):
#     return (2 * index) + 1

# def right(index):
#     return (2 * index) + 2

# def parent(index):
#     return (index - 1) // 2

# def _buildRecursive(array, index):

#     end = len(array)
#     leftC = left(index)
#     rightC = leftC + 1
#     print(leftC, index)

#     if (leftC <= end-1):
#         if (array[leftC] > array[rightC]):
#             largest = leftC

#         else:
#             largest = rightC
#     else:
#         return
#     # if (array[leftC] < array[rightC]):
#     #     largest = rightC
#     # else:
#     #     largest = leftC

#     if largest != index:
#         array[largest], array[index] = array[index], array[largest]
#         _buildRecursive(array, largest)

# def buildRecursive(array):
#     end = len(array)-1
#     for i in range(ceil(end / 2) , 0 , -1 ):
#         _buildRecursive(array, i)

#     return array

# def heapsort(array):
#     array = buildRecursive(array)
#     virtualLength = len(array) - 1
#     while virtualLength > 0:  # Iterating backwards through the list

#         if array[0] == array[virtualLength]:  # If there is a duplicate skip it
#             virtualLength -= 1
#             pass

#         array[0], array[virtualLength] = array[virtualLength], array[0]
#         index = 0
#         largest = 0
#         while True:
#             leftC = left(index)
#             rightC = leftC + 1
#             if (leftC < virtualLength and array[leftC] > array[index]):
#                 largest = leftC
#             else:
#                 largest = index

#             if (rightC < virtualLength and array[rightC] > array[largest]):
#                 largest = rightC
#             if largest == index:  # If the current index is larger than its kids break the loop
#                 break

#             array[largest], array[index] = array[index], array[largest]
#             index = largest
#             '''
#                 Attempting to check just one child
#             '''
#             # if (leftC < virtualLength-1) and (array[leftC] < array[leftC+1]):
#             #     leftC += 1

#             # if (leftC < virtualLength) and array[largest] < array[leftC]:
#             #     array[largest], array[leftC] = array[leftC], array[largest]

#             # largest = leftC
#             # if leftC >= 1:
#             #     break

#         virtualLength -= 1

#     return array

# from math import ceil
# from time import perf_counter
# import random

# import quicksort
'''
----------------------https://www.geeksforgeeks.org/heap-sort/
'''
# def heapify(arr, n, i):
#     largest = i # Initialize largest as root
#     l = 2 * i + 1     # left = 2*i + 1
#     r = l + 1     # right = 2*i + 2

#     # See if left child of root exists and is
#     # greater than root
#     if l < n and arr[i] < arr[l]:
#         largest = l

#     # See if right child of root exists and is
#     # greater than root
#     if r < n and arr[largest] < arr[r]:
#         largest = r

#     # Change root, if needed
#     if largest != i:
#         arr[i],arr[largest] = arr[largest],arr[i] # swap

#         # Heapify the root.
#         heapify(arr, n, largest)

# # The main function to sort an array of given size
# def heapsort(arr):
#     n = len(arr)

#     # Build a maxheap.
#     for i in range(n, -1, -1):
#         heapify(arr, n, i)

#     # One by one extract elements
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i] # swap
#         heapify(arr, i, 0)
#     return arr
'''
----------------------
'''
'''
 Original attempt
'''


# find left right and parent nodes respectively retunrs theur index
# def left(index):
#     return (2 * index) + 1


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