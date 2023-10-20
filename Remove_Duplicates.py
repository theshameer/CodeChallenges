"""
Remove the duplicates from a list of integers, keeping one occurrence of each element.
"""
def solve(arr):
    arr = set(arr)
    arr_result = []

    for i in arr:
        arr_result.append(i)
    
    return arr_result
