# Cycle Finding using recursion which has the time complexity of O(E) and space complexity of O(V)
def cycle(graph, node,visited_set,parent):
    if(node not in visited_set):  
       visited_set.add(node)
    for i in graph[node]:
        if(i not in visited_set):
            result=cycle(graph, i,visited_set,node)
            if(result):
                return True
        elif(i!=parent): 
            return True 
    return False

graph={1:[2],2:[1,3],3:[1],5:[6],6:[5]}
visited_set=set()  
flag=False
for i in graph:
    if(i not in visited_set):
        if cycle(graph, i,visited_set,None) :
            flag=True
            break
    
print(flag) 