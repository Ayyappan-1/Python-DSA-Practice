# DFS using recursion which has the time complexity of O(E) and space complexity of O(V)
def dfs(graph,node, visited_set,visited):  
    visited_set.add(node)
    visited.append(node)
    for i in graph[node]:
        if(i not in visited_set):
            dfs(graph,i, visited_set,visited) 
    return visited

graph={1:[2],2:[1,3],3:[],5:[6],6:[5]}
visited_set=set()
visited=[]

for i in graph:
    if(i not in visited_set):
        dfs(graph,i,visited_set,visited)
print(visited)
