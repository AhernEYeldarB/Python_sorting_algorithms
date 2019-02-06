'''
    https://www.geeksforgeeks.org/iterative-quick-sort/
'''
from random import randint


def quicksort(array):
    end = len(array) - 1
    start = 0

    # Init stack
    length = end - start + 1
    stack = [0] * (length)

    # initialize top of stack
    top = -1

    # push initial values of start and end to stack
    top = top + 1
    stack[top] = start
    top = top + 1
    stack[top] = end

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop end and start
        end = stack[top]
        top = top - 1
        start = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = _partition(array, start, end)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > start:
            top = top + 1
            stack[top] = start
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < end:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = end

    return array


def _partition(inList, start, end):
    '''
        Function to calculate the partition in a quicksort 
        (Should be pseudorandomly generated and not liner for best expected performance)
    '''
    # Random Pivot implementation
    randomPivot = randint(start, end)
    inList[randomPivot], inList[start] = inList[start], inList[randomPivot]

    pivot = start
    temp = inList[start]

    # newPiv = inList[pivot]
    for i in range(start + 1, end + 1):
        if inList[i] <= temp:
            pivot += 1
            inList[i], inList[pivot] = inList[pivot], inList[i]

    inList[pivot], inList[start] = inList[start], inList[pivot]

    return pivot