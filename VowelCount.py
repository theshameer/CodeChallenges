



##def vowelcount(userinput):
##
##    count = 0
##
##    vowels = ["a","e","i","o","u"]
##
##
##    for i in userinput:
##        if i in vowels:
##            count= count +1
##
##    return count
##        
##
##
##
##
##
##
##for i in range(5):
##    userstr = input("Input a string: ")
##    print(vowelcount(userstr))
##
##        

import traceback

class VowelCount:

    vowels= ["a","e","i","o","u"]


    def __init__(self, userstr):
        self.storeduserstr = userstr


    def __str__(self):
        return f"user's string = {self.storeduserstr}."




    def vowelcount(self):
        count = 0
        try:
            for i in self.storeduserstr:
                if i in self.vowels:
                    count= count +1
        except TypeError as e:
            print(f"TypeError: Enter a string : {e.__traceback__.tb_frame}, \n{e.__traceback__.tb_lasti},\n {e.__traceback__.tb_lineno},\n {e.__traceback__.tb_next} ")
            stack_frames = traceback.extract_tb(e.__traceback__)

            # Print each stack frame
            for frame in stack_frames:
                filename, line_number, function_name, text = frame
                print(f"File: {filename}, Line: {line_number}, Function: {function_name}, Code: {text}")


        return count


j = VowelCount(123)


print(j.vowelcount())

print(j)
            
