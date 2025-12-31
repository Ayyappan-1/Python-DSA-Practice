# Linked list deletion at position and displaying which has the time complexity of O(n) and Space complexity of O(1)
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

    def delete_at_position(self, pos):
        current_node=self.head
        
        if(pos>=0 and pos<self.size):
            if(pos==0):
                self.head=current_node.next
                current_node.next=None
                return
            i=0
            while(i<pos-1):
                current_node=current_node.next
                i+=1
            delete_node=current_node.next
            current_node.next=delete_node.next
            delete_node.next=None
            self.size-=1
        else:
            print("Invalid Position")

    def display(self):
        current=self.head 
        while current!=None:
            print(current.data)
            current=current.next

l1=Linked_List()
l1.insert_at_head(10)
l1.insert_at_head(20)
l1.insert_at_head(30)
l1.delete_at_position(0)
l1.display()