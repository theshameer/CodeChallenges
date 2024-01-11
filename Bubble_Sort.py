"""
This algorithm is the algorithm for bubble sort
"""

def BubbleSort(arr):
    pointer = 0
    for i in range(len(arr)):
        for j in arr:
            if pointer == len(arr)-1:
                pointer = 0
                break
            if arr[pointer] > arr[pointer+1]:
                m = arr[pointer+1]
                arr[pointer+1] = arr[pointer]
                arr[pointer] = m
                pointer+=1
            elif arr[pointer] <= arr[pointer+1]:
                pointer +=1
    return arr

print(BubbleSort([2,4,1,3,5,3,32,43,1,94,23894,56,2376,3467,2346789,234897,134789,78934,34897,894,7843,34578,287,498,28,23,342]))
