"""
BFS graph traversal using a list to mimic a queue
"""
traversal = False

graph = {"A":["B","E","G"],
         "B": ["A","C","G","F","H"],
         "C":["B","D","H"],
         "D":["C","E"],
         "E":["A","D","F"],
         "F":["B","E"],
         "G":["A","B"],
         "H":["B","C"]
         }

queue = []
visited_list = []
visiting = "A"
print(graph["A"])
print(len(graph))



while traversal != True:
    visited_list.append(visiting)
    print(f"visited list = {visited_list}")
    
    if len(visited_list) == len(graph):
        traversal = True
    for i in graph[visiting]:
        if i not in visited_list and i not in queue: 
            queue.append(i)
            print(f"queue = {queue}")
            
    if len(queue) == 0:
        break
        
    visiting = queue[0]
    queue.pop(0)

print(visited_list)
