"""
The cat wants to lay down on the table, but the problem is that we don't know where it is in the room!

You'll get in input:

the cat coordinates as a list of length 2, with the row on the map and the column on the map.
the map of the room as a list of lists where every element can be 0 if empty or 1 if is the table (there can be only one 1 in the room / lists will never be empty).
Task:
You'll need to return the route to the table, beginning from the cat's starting coordinates, as a String. The route must be a sequence of letters U, D, R, L that means Up, Down, Right, Left. The order of the letters in the output isn't important.

Outputs:
The route for the cat to reach the table, as a string
If there isn't a table in the room you must return "NoTable"
if the cat is outside of the room you must return "NoCat" (this output has the precedence on the above one).
If the cat is alredy on the table, you can return an empty String.
Example:
cat = [0,1]
room =[[0,0,0], [0,0,0], [0,0,1]]

The route will be "RDD", or "DRD" or "DDR"

"""
def put_the_cat_on_the_table(cat, room):
    sub_list_index = 0
    list_index = 0
    count = -1
    result = ""
    

    
    if cat[0]> (len(room)-1) or cat[0]<0:
        return "NoCat"
    for i in room:
        if (len(i)-1)<cat[1] or 0>cat[1]:
            return "NoCat" 
    
    
    
    NoTable = True
    
    
    
    for i in room:
        count+=1
        if int(1) in i:
            sub_list_index = room[count].index(1)
            list_index = count
            NoTable = False
    
    if NoTable == True:
        return "NoTable"
        
            
    list_difference = list_index - cat[0]
    sub_list_difference = sub_list_index - cat[1]

    
    if sub_list_difference >= 1:
        while sub_list_difference != 0:
            result += "R"
            sub_list_difference-=1
            
    elif sub_list_difference <= 1:
        while sub_list_difference != 0:
            result += "L"
            sub_list_difference+=1
    
    if list_difference >= 1:
        while list_difference != 0:
            result += "D"
            list_difference-=1
            
    elif list_difference <= 1:
        while list_difference != 0:
            result += "U"
            list_difference+=1    



    
    return result

"""
Tests
"""
import codewars_test as test
from solution import put_the_cat_on_the_table
from collections import Counter

def assert_fuzzy_equals(act, exp):
    if exp in ("NoCat", "NoTable"):
        test.assert_equals(act, exp, "Should return the correct solution")
    elif not isinstance(act,str) or Counter(act)!=Counter(exp):
        test.assert_equals(act, exp, "The expected output is only one of the possibilities")
    else:
        test.assert_equals(Counter(act) == Counter(exp), True)
    
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        room = [
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,1]
              ]
        assert_fuzzy_equals(put_the_cat_on_the_table([0,0], room), "RRRDD")


        room = [
               [0,0,0,0,0,0]
              ]
        assert_fuzzy_equals(put_the_cat_on_the_table([0,2], room), "NoTable")






