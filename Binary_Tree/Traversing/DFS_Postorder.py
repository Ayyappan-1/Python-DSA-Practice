# DFS Postorder which has the time complexity of O(n) and space complexity of O(n)
def postorder(n,current_node):
    if(current_node>n):
        return
    if(binary_tree[current_node]==None):
        return
     
    postorder(n,2*current_node+1)
    postorder(n,2*current_node+2)    
    print(binary_tree[current_node])

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

postorder(n,0)