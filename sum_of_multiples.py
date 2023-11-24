"""
Find the sum of all multiples of n below m

n and m are natural numbers (positive integers)
m is excluded from the multiples

Examples
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"
"""

def sum_mul(n, m):
    output = 0
    
    if m<=0 or n<=0:
        return "INVALID"
    
    if n > m or n==m:
        return 0

    
    
    for i in range(n, m):
        if i % n == 0:
            output+=i
            
    return output
