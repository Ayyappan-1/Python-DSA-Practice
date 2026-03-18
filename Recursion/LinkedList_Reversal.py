class Node :
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_head(self,element):
        new_node=Node(element)
        new_node.next=self.head
        self.head=new_node

    def reversal(self,current,previous): 
        if(current==None):
            return previous 
        next_node=current.next
        current.next=previous
        previous=current
        current=next_node 
        return self.reversal(current, previous)
    new_root=reversal(root,None)