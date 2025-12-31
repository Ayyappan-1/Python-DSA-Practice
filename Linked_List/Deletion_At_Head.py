# Linked list deletion at head and displaying which has the time complexity of O(1) and Space complexity of O(1)
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None
        self.size=0

    def insert_at_head(self,data):
        next_node=Node(data)
        next_node.next=self.head
        self.head=next_node
        self.size+=1

    def deletion_at_head(self):
        current=self.head
        if(self.size>0):
            self.head=current.next
            current.next=None
            self.size-=1
        else:
            print("Linked List Is Empty....")

    def display(self):
        current=self.head 
        while current!=None:
            print(current.data)
            current=current.next
l1=Linked_List()
l1.insert_at_head(10)
l1.insert_at_head(20)
l1.insert_at_head(30)
l1.deletion_at_head()
l1.display()