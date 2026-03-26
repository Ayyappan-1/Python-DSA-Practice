# Undirected Graph implementation which has the time complexity O(e) and Space complexity of O(e+n)
def undirected_graph(a):
    Undirected={}
    for i in a:
        if(i[0] in Undirected):
            Undirected[i[0]].append(i[1]) 
        else:
            Undirected[i[0]]=[i[1]] 
        if(i[1] in Undirected):
               Undirected[i[1]].append(i[0])
        else:
                Undirected[i[1]]=[i[0]]
    return Undirected

# Directed Graph implementation which has the time complexity O(e) and Space complexity of O(e+n)
def directed_graph(a):
    directed={}
    for i in a:
        if(i[0] in directed):
            directed[i[0]].append(i[1])
        else:
            directed[i[0]]=[i[1]]
        if(i[1] not in directed):
            directed[i[1]]=[]
    return directed

a=[[1,2],[2,3]]
Undirected=undirected_graph(a)
directed=directed_graph(a)
print("Undirected Graph")
for vertex,edges in Undirected.items():
    print(f"{vertex} : {edges}")

print("Directed Graph")
for vertex,edges in directed.items():
    print(f"{vertex} : {edges}")

