"""
ROT13 is a simple letter substitution cipher that replaces a letter with the 
letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""



import string

def rot13(message):
    alphabet = []
    
    result = ""
    upper_or_not = False
    
    for i in string.ascii_lowercase:
        alphabet.append(i)
        
    for i in message:
        
        upper_or_not = i.isupper()
        i = i.lower()
        
        if i in alphabet:
            for index,letter in enumerate(alphabet):
                if letter == i:
                    m = (index + 13) % 26
                    if upper_or_not == True:
                        result+=alphabet[m].upper()
                    elif upper_or_not == False:
                        result+=alphabet[m]
        elif i not in alphabet:
            result+=i
    
    return result
                    
