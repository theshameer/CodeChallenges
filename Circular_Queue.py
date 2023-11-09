"""
This program displays the python implementation of a circular queue
"""
class Queue:
    MAX_SIZE = 10
    queue =[""]*MAX_SIZE
    front = -1
    rear = -1

my_queue = Queue()

def is_full():
    if ((my_queue.rear+1) % my_queue.MAX_SIZE) == my_queue.front:
        return True
        

def is_empty():
    if my_queue.front == -1:
        return True

def enqueue(item):
    if is_full() == True:
        raise Exception("Queue is full, cannot enqueue")
    else:
        my_queue.rear = (my_queue.rear+1) % my_queue.MAX_SIZE
        my_queue.queue[my_queue.rear] = item
        if my_queue.front == -1:
            my_queue.front = 0

def dequeue():
    if is_empty() == True:
        raise Exception("Queue is empty, cannot dequeue")
    else:
        dequeued_item = my_queue.queue[my_queue.front]
        my_queue.queue[my_queue.front] = ""

        if my_queue.front == my_queue.rear:
            my_queue.front = - 1
            my_queue.rear = -1
        else:
            my_queue.front = (my_queue.front+1) % my_queue.MAX_SIZE
        
        return dequeued_item 

def peek():
    return my_queue.queue[my_queue.front]
