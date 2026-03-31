# Number of Island using recursion which has the time complexity of O(R x C) and space complexity of O(R x C)
def dfs(matrix,i,j ):       
    if(i<0 or j<0 or i>=row or j>=column):
        return
    if(matrix[i][j]==0):
        return
    matrix[i][j]=0
    dfs(matrix,i-1,j)
    dfs(matrix,i+1,j)
    dfs(matrix,i,j-1)
    dfs(matrix,i,j+1) 

def island(matrix):
    count=0 
    row=len(a[0])
    for i in range(column):
        for j in range(row):
           if(a[i][j]==1 ):
              count+=1
              dfs(a,i,j)
    return count

a=[
    [1,1,0,0],
    [1,1,0,0],
    [0,0,1,0],
    [1,1,0,0]
]  
column=len(a)
row=len(a[0])
print(island(a))