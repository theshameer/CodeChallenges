"""
Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.

Valid examples, should return true:

"""

s = "   565543    "

x = s.rstrip(" ")
t = x.lstrip(" ")
    	
print(t)
result = t.isnumeric()



if result == "True":
    print("true")
elif result != "False":
    print("false")
