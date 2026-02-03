# DFS Preorder which has the time complexity of O(n) and space complexity of O(n)
def preorder(n,current_node):
    if(current_node>n):
        return
    if(binary_tree[current_node]==None):
        return
     
    print(binary_tree[current_node])
    preorder(n,2*current_node+1)
    preorder(n,2*current_node+2)    

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

preorder(n,0)