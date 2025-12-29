# Linked list insertion at head and displaying which has the time complexity of O(1) and Space complexity of O(1)

# Node class is to create N number of nodes necessary for our linked list and each node is considered to be a object of node..
class node :
    def __init__(self,data):
        self.data=data
        self.next=None

# Linked_list is is the heart and responsible for creation of a linked list and assigning head reference with all other operations.
class linked_list:
    def __init__(self):
        self.head=None

    def insert_at_head(self,data):
        next_node=node(data)
        next_node.next=self.head
        self.head=next_node

    def display(self):
        current=self.head 
        while current!=None:
            print(current.data)
            current=current.next

# Creating a linked list by creating a object. Later inserting elements like 1,2,3 and displaying them. 
l1=linked_list()
l1.insert_at_head(1)
l1.insert_at_head(2)
l1.insert_at_head(3)
l1.display()

# My first problem using OOPs concepts like objects, classes, instance methods and constructor. 