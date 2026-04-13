# Biggest Island using recursion which has the time complexity of O(R x C) and space complexity of O(R x C)

def dfs(matrix,i,j,c ):       
    if(i<0 or j<0 or i>=row or j>=column):
        return c
    if(matrix[i][j]==0):
        return c
    c+=1
    matrix[i][j]=0
    c=dfs(matrix,i-1,j,c)
    c=dfs(matrix,i+1,j,c)
    c=dfs(matrix,i,j-1,c)
    c=dfs(matrix,i,j+1,c) 
    return c

def island(matrix):
    max_count=0,0
    row=len(a[0])
    for i in range(column):
        for j in range(row):
           if(matrix[i][j]==1 ): 
              max_count=max(max_count,dfs(a,i,j,0)) 
    return max_count

a=[
    [1,1,0,0],
    [1,1,1,0],
    [0,0,1,0],
    [1,1,0,0]
]  
column=len(a)
row=len(a[0])
print(island(a))