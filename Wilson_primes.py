"""
Wilson primes satisfy the following condition. Let P represent a prime number.

Then,

((P-1)! + 1) / (P * P)
should give a whole number.

Create a function that returns true if the given number is a Wilson prime.
"""
import math

def am_i_wilson(n):
    
    if n == 0 or n==1:
        return False
    
    
    
    
    if ((math.factorial(n-1) + 1)/(n * n) %1) != 0:
        return False
    else:
        return True
