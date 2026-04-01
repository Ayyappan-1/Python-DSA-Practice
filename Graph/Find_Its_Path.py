# Find existence of path between two nodes in a graph using recursion which has the time complexity of O(E) and space complexity of O(E)

def find(graph, visited,node,target):
    if(node==target):
        return True
    for i in graph[node]:
        if(i not in visited):
            visited.add(i)
            if(find(graph,visited, i, target)):
                return True
    return False

start=5
target=6
graph={1:[2],2:[1,3],3:[],5:[6],6:[5]}
visited=set()

print(find(graph,visited,start, target))