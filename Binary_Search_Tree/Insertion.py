# Insertion in binary search tree by using parent tracking which has the time complexity of O(H) and space complexity of O(1)
from collections import deque
class bst:
    def __init__(self):
        self.root=None

class Node:
    def __init__(self,ele):
        self.left=None
        self.right=None
        self.data=ele

    def insertion(self, root, element):
        new_node=Node(element)
        parent=None
        current=root
        if (root is None):
            return new_node
        while current:
            if(current.data>element):
                parent=current
                current=current.left
                if(current is None):
                    parent.left=new_node
                    return 
            else:
                parent=current
                current=current.right
                if(current is None):
                    parent.right=new_node
                    return 

                