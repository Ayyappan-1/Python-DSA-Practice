# Insertion at tail which has the time complexity of O(n) and Space compelxity of O(1)

# Node class is to create N number of nodes necessary for our linked list and each node is considered to be a object of node.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Linked_list is is the heart and responsible for creation of a linked list and assigning head reference with all other operations.
class Linked_List:
    def __init__(self):
        self.head=None

    def insert_at_tail(self,data):
        new_node=Node(data)
        if self.head!=None :
           current_node=self.head
           while current_node.next !=None:
               current_node=current_node.next
           current_node.next=new_node
        else:
            self.head=new_node
            

    def display(self):
        current=self.head 
        while current!=None:
            print(current.data)
            current=current.next

# Creating a linked list by creating a object. Later inserting elements similar to list appending. 
l1=Linked_List()
l1.insert_at_tail(1)
l1.insert_at_tail(2)
l1.insert_at_tail(3)
l1.display()
