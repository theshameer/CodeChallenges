"""
This algorithm is linear search
"""

def LinearSearch(arr,target_val):

    for i in arr:
        if i == target_val:
            return f"Target Value found at index: {arr.index(target_val)}"
        elif (arr.index(i) == len(arr)-1) and (i != target_val):
            return "Target Value not in list"
        
print(LinearSearch([4,1,5,7,6,21,45,2],70))

