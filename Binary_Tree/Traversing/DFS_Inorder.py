# DFS Inorder which has the time complexity of O(n) and space complexity of O(n)
def inorder(n,current_node):
    if(current_node>n):
        return
    if(binary_tree[current_node]==None):
        return
     
    inorder(n,2*current_node+1)
    print(binary_tree[current_node])
    inorder(n,2*current_node+2) 

def insertion(n,ele):
    n+=1
    binary_tree[n]=ele
    return n

    
binary_tree=[None]*100
n=-1
n=insertion(n,1)
n=insertion(n,2)
n=insertion(n,3)
n=insertion(n,4)
n=insertion(n,5)
n=insertion(n,6)

inorder(n,0)