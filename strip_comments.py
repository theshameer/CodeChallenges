"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
"""

def strip_comments(strng, markers):
    
    strng = list(str(strng))
    s = ""
    
    
    for i in markers:
        if i in strng:
            strng.remove(i)
        
    while strng[-1] == " ":
        strng.pop(-1)
    
    for i in strng:
        s+=i
    

    
    return s
