"""
This program find the factors of any inputted number until a certain factor is reached and then outputs a set of these numbers
"""

def factors(integer, limit):
    
    result_array = []
    for i in range(limit, (integer+1)):
        if integer%i == 0:
            result_array.append(int(i))
            result_array.append(int(integer/i))
            
    return set(result_array)
