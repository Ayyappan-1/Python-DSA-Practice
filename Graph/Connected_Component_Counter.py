# Counting connected components in a undirected graph which has the time complexity of O(E + V) and space complexity of O(V)
def counter(graph,node,visited):
    if(node not in visited):
        visited.add(node)
    for i in graph[node]:
        if(i  not in visited):
            visited.add(i)
            counter(graph,i,visited)
    return visited

visited=set()
count=0
graph={1:[2],2:[1,3],3:[],5:[6],6:[5]}

for i in graph:
    if(i not in visited):
        count+=1
    visited=counter(graph, i, set())

print(count)
