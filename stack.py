"""
This code is the python implementation of a stack
"""
class Stack:
    MAX_SIZE = 10
    top_pointer = -1
    stack = [""]*MAX_SIZE

my_stack = Stack()

def is_full():
    if my_stack.top_pointer  == my_stack.MAX_SIZE - 1:
        return True


def is_empty():
    if my_stack.top_pointer  == -1:
            return True
    

def push(item):
     
    if is_full() == True:
        raise Exception("Stack is full, cannot push item")
    else:
        my_stack.top_pointer += 1
        my_stack.stack[my_stack.top_pointer] = item



def pop():
    if is_empty() == True:
        raise Exception("Stack is empty, cannot pop item")
    else:
        popped_item = my_stack.stack[my_stack.top_pointer]
        my_stack.top_pointer -= 1
        my_stack.stack[my_stack.top_pointer + 1] = ""
        return popped_item
    
def peek():
    return my_stack.stack[my_stack.top_pointer]
