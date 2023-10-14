"""
You are given a string of space separated numbers, and have to return the highest and lowest number.
"""


def high_and_low(numbers):
    print(numbers,numbers.split(" "))
    converted_numbers = list(map(int, numbers.split(" ")))


    
    var_low = converted_numbers[0]
    var_high = converted_numbers[0]
    
    
    for i in converted_numbers[1:] :
        if i < var_low:
            var_low = i
            
        elif i > var_high:
            var_high = i
            
    return str(f"{var_high} {var_low}")
