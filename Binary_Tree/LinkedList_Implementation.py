# Node creation for our binary tree.

from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

# Binary Tree class is responsible for creating binary trees.
class BinaryTree:
    def __init__(self):
        self.root=None

 # Insertion operation which has the time complexity of O(n) and space complexity of O(n)
    def insertion(self,data):
        new_node=Node(data)
        if self.root==None:
            self.root=new_node
            return
        queue=deque()
        queue.append(self.root)
        while queue:
            current=queue.popleft()
            if current.left==None:
                current.left=new_node
                return
            else:
                queue.append(current.left)
            if current.right==None:
                current.right=new_node
                return
            else:
                queue.append(current.right)

 # Deletion operation which has the time complexity of O(n) and space complexity of O(n)
    def deletion(self,data):
        if self.root==None:
            return

        queue=deque()
        queue.append(self.root)

        delete_node=None
        last_node=None
        parent_of_last=None

        while queue:
            current=queue.popleft()

            if current.data==data:
                delete_node=current

            if current.left:
                parent_of_last=current
                last_node=current.left
                queue.append(current.left)

            if current.right:
                parent_of_last=current
                last_node=current.right
                queue.append(current.right)

        if delete_node==None:
            return

        delete_node.data=last_node.data

        if parent_of_last.left==last_node:
            parent_of_last.left=None
        else:
            parent_of_last.right=None

 # Traversal operation which has the time complexity of O(n) and space complexity of O(n)
    def level_order(self):
        if self.root==None:
            return
        queue=deque()
        queue.append(self.root)
        while queue:
            current=queue.popleft()
            print(current.data,end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

bt=BinaryTree()

while True:
    print("\nMenu\n1.insert\n2.delete\n3.display\n4.exit")
    choice=input()
    match choice:
        case '1':
            bt.insertion(int(input()))
        case '2':
            bt.deletion(int(input()))
        case '3':
            bt.level_order()
        case '4':
            break
