"""
Create a method to see whether the string is ALL CAPS.
"""
def is_uppercase(inp):
    if isinstance(inp,str) == False:
        return True
        
    return inp.isupper()
