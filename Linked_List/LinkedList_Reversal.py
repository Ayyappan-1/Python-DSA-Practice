# Reversing a linked list by using two pointer method which has the time complexity of O(n) and space complexity of O(1)
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None
        
    def insert_at_head(self,data):
        next_node=Node(data)
        next_node.next=self.head
        self.head=next_node

    def reverse(self):
        if(self.head==None):
            print("The list is empty")
            return
        curr_node=self.head
        prev_node=None
        while(curr_node!=None):
            next_mode=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_mode
        self.head=prev_node 

    def display(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next

l1=Linked_List() 
l1.insert_at_head(30)
l1.insert_at_head(20)
l1.insert_at_head(10) 
l1.insert_at_head(5) 
l1.insert_at_head(2) 
l1.reverse()
l1.display()
            
        