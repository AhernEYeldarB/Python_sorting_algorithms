def insertSort(array, start, end):
    # if end == 0:
    #     end = len(array)

    for i in range(start , end):
        current = array[i]
        prev = i - 1

        while (array[prev] > current) and (prev >= start):
            array[prev + 1] = array[prev]
            prev -= 1

        array[prev + 1] = current

    return array