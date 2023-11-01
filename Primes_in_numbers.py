"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
 
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

"""

def prime_factors(n):
    
    if n <= 1:
        return []
    result_array = []

    result_str = ""
    
    original_num = n
    
    divisor = 1

    
    for i in range(2, int((original_num**0.5)+1)):
        divisor = i
        if (i > 2) and (i % 2 == 0):
            continue
#         print(f"n: {n}, i: {i}")
        if n < i:
            break
        if n % i == 0:
            while n % i == 0:
                result_array.append(i)
                n = n//i
#                 print(f"new n: {n}, i: {i}")
    
    if n > divisor and n > 1:
        result_array.append(n)

                
    
    if len(result_array) == 0:
        result_array.append(n)
    
    result_set = sorted(set(result_array))
    print(result_set)
    print(result_array)
    
    
    for i in result_set:
        if result_array.count(i)>1:
            result_str+=f"({i}**{result_array.count(i)})"
        
        elif result_array.count(i) ==1 :
            result_str+=f"({i})"
    
    return result_str
