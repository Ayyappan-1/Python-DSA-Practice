# Insertion at a specific position which has the time complexity of O(n) and space complexity of O(1)
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None
        self.size=0

    def  insert_at_position(self,data,pos):
        new_node=Node(data) 
        current=self.head
        if(pos>=0  and pos<=self.size):
           if(pos==0):
               new_node.next=self.head
               self.head=new_node 
           else: 
              for i in range(0,pos-1):
                  current=current.next
              new_node.next=current.next
              current.next=new_node
           self.size+=1
        else:
            print("Wrong position was given.........")

    def display(self):
        current=self.head 
        while current!=None:
            print(current.data)
            current=current.next

l1=Linked_List() 
l1.insert_at_position(1,0)
l1.insert_at_position(2,1)
l1.insert_at_position(3,1)
l1.display()