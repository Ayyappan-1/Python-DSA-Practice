# Binary tree height which has the time complexity of O(n) and space complexity of O(n)
from collections import deque
def btree_height(root) :
    if (not root):
        return
    count,element=0,1
    q=deque() 
    while q :
        for _ in len(q):
            current=q.popleft()
            if(current.left):
                q.append(current.left)
            if(current.right):
                q.append(current.right)
        count+=1
