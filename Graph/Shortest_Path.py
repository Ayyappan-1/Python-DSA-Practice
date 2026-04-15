# Shortest path using BFS traversal algorithm which has the time complexity of O(V+E) and space complexity O(V)
from collections import deque
def shortest_path (graph,start, target): 
    count=0
    visited=set()
    queue=deque()
    queue.append(start)  
    visited.add(start)
    while queue:
        length=len(queue)
        for _ in range(length):
            popped=queue.popleft() 

            if(popped==target):
               return  count 
            for i in graph[popped]:
               if(i not in visited):
                  visited.add(i)
                  queue.append(i)
        count+=1  
    return False

count=0
graph={1:[2,3],2:[1],3:[1,5],5:[6],6:[5]}
distance=shortest_path(graph, 1,60)
print(distance) if(distance) else print("No such target found !")