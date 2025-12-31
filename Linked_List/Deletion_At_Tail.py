# Linked list deletion at tail and displaying which has the time complexity of O(n) and Space complexity of O(1)
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
       

    def delete_at_tail(self):
        if(self.head==None):
            print("Nothing to delete, Linked list is Empty !")
            return
        current_node=self.head
        if(current_node.next==None):
            self.head=None
            return
        while(current_node.next.next!=None): 
            current_node=current_node.next
        current_node.next=None
        
    def display(self):
        current=self.head 
        while current!=None:
            print(current.data)
            current=current.next
        
l1=Linked_List()
l1.insert_at_head(30)
l1.insert_at_head(20)
l1.insert_at_head(10)
l1.delete_at_tail()
l1.delete_at_tail()
l1.display()