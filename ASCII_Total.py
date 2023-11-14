"""
You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all printable ASCII characters.
"""

def uni_total(s):
    
    val = 0
    for i in str(s):
        val+= ord(i)
        
    return val
