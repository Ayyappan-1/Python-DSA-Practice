# BFS without using recursion which has the time complexity of O(v^2) and space complexity of O(v)
from collections import deque
def bfs (adjacency_list):
    a=deque()
    visited=[]
    for i in adjacency_list:
            a.append(i)
            if(i not in visited):
               visited.append(i)
            while a:
                 popped_node=a.popleft() 
                 for i in adjacency_list[popped_node]: 
                      if(i not in visited):
                          visited.append(i)
                          a.append(i)

    return visited

visited=bfs({1:[2],2:[1,3],3:[],5:[6],6:[5]})
print(visited)