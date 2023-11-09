"""
This shows the python implementation of a linear queue
"""

class Queue:
    MAX_SIZE = 10
    queue =[""]*MAX_SIZE
    front = 0
    rear = -1

my_queue = Queue()

def is_full():
    if my_queue.MAX_SIZE == (my_queue.rear+1):
        return True

def is_empty():
    if my_queue.front > my_queue.rear:
        return True

def enqueue(item):
    if is_full() == True:
        raise Exception("Queue is full, cannot enqueue")
    else:
        my_queue.rear+=1
        my_queue.queue[my_queue.rear] = item

def dequeue():
    if is_empty() == True:
        raise Exception("Queue is empty, cannot dequeue")
    else:
        my_queue.front+=1
        my_queue.queue[(my_queue.front - 1)] = ""

def peek():
    return my_queue.queue[my_queue.front]
