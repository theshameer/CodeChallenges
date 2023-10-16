"""
Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.
"""


def neutralise(s1, s2):
    
    result_string = ""
    
    for i,j in zip(s1,s2):
        if i == j:
            result_string+=i
        else:
            result_string+="0"
    
    return result_string
