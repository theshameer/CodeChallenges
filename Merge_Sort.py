"""
This algorithm is the algorithm for Merge Sort
"""

from random import randint
import random





def MergeSort(arr):
  if len(arr)== 1:
    return arr
  mid = len(arr) //2
  left = MergeSort(arr[0:mid])
  right = MergeSort(arr[mid:len(arr)])
  return Merge(left,right)





def Merge(list_a, list_b):
  merged =[]
  while len(list_a)>0 and len(list_b)>0:
    if list_a[0] < list_b[0]:
      merged.append(list_a[0])
      list_a.remove(list_a[0])
    else:
      merged.append(list_b[0])
      list_b.remove(list_b[0])

  if len(list_a)>0:
    merged=merged + list_a
  elif len(list_b) > 0:
    merged = merged + list_b

  return merged

#print(Merge([random.randint(1,1000) for i in range(100)], [random.randint(1,1000) for i in range(100)]))


print(MergeSort([random.randint(1,1000) for i in range(100)])) 
