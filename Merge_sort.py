"""
This is the merge sort algorithm implemented recursively
"""
def merge(left,right):
    
    merged = []
    index_left = 0
    index_right = 0
    
    while index_left <len(left) and index_right<len(right):
        
        if left[index_left]<right[index_right]:
            merged.append(left[index_left])
            index_left += 1
        
        else:
            merged.append(right[index_right])
            index_right +=1
    
    while index_left <len(left):
        merged.append(left[index_left])
        index_left +=1
        
        
    while index_right < len(right):
        merged.append(right[index_right])
        index_right +=1
    
    
    return merged
    
def merge_sort(items):

 
    if len(items) <= 1:
        return items
    else:
        midpoint = (len(items)-1) // 2 
        left_half = items[0:midpoint+1]
        right_half = items[midpoint+1:len(items)] 
        
        left_half = merge_sort(left_half) 
        right_half = merge_sort(right_half) 
        
        
        merged_items = merge(left_half, right_half) 

        return merged_items
