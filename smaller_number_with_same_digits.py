"""
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017


Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.


next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
"""
import random
import itertools

def next_smaller(n):
    string_original_num = str(n)
    new_num = 0
    return_num = 0
    seed_list = []
    
    for i in range(0,len(str(n))):
        seed_list.append(i)
    
    my_2d_array = list(itertools.permutations(seed_list, len(seed_list)))


    
    for row in my_2d_array:
        string_num = ""
        for index,element in enumerate(row):
            string_num+=string_original_num[element]
            
        
        
        
        if int(string_num)<n and len(str(int(string_num))) == len(seed_list) and int(string_num) > new_num :
            new_num = int(string_num)
        
    

    if new_num == 0:
        new_num = -1
    
    return new_num




def example_cases():
  test.assert_equals(next_smaller(907), 790)
  test.assert_equals(next_smaller(531), 513)
  test.assert_equals(next_smaller(135), -1)
  test.assert_equals(next_smaller(2071), 2017)
  test.assert_equals(next_smaller(414), 144)
