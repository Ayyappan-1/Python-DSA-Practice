# Flood fill using recursion which has the time complexity of O(R x C) and space complexity of O(R x C)
def flood(graph,i,j):
    if(i<0 or j<0 or i>=row or j>=column):
        return 
    if(graph[i][j]==0 or graph[i][j]==2):
        return 
    
    graph[i][j]=2
    flood(graph,i+1,j)
    flood(graph,i-1,j)
    flood(graph,i,j+1)
    flood(graph,i,j-1)
    return graph


a=[
    [1,1,0,0],
    [1,1,0,0],
    [0,0,1,0],
    [1,1,0,0]
]  
row=len(a)
column=len(a[0])
for i in range(row):
    for j in range(column):
        if(a[i][j]==1):
           a=flood(a,i,j)
           
        
print(a)