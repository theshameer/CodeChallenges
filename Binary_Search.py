"""
This algorithm is the algorithm for Binary Search
"""

def BinarySearch(arr, target_val):

    top_pointer = len(arr)-1
    bottom_pointer = 0

    val_found = False
    middle_pointer = 0

    while val_found == False:
        middle_pointer = (top_pointer - bottom_pointer)//2

        if arr[middle_pointer] == target_val:
            val_found = True
        elif target_val > arr[middle_pointer]:
            bottom_pointer = middle_pointer
        elif target_val < arr[middle_pointer]:
            top_pointer = middle_pointer


        if ((top_pointer - bottom_pointer) <= 2) and (arr[middle_pointer] != target_val):
            return "Target Value not found"




    if val_found == True:
        return f"Target Value found at index {middle_pointer}"
    

print(BinarySearch([2,3,5,6,7,8,9,11,13],4))
