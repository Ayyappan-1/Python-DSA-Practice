# Searching a element in linked list which has the time complexity of O(n) and space complexity of O(1)
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

    def search(self,target):
        current=self.head 
        index=0
        while current!=None: 
            if(current.data==target):
                return index
            current=current.next
            index+=1
        return -1

l1=Linked_List()
l1.insert_at_head(30)
l1.insert_at_head(20)
l1.insert_at_head(10) 
target=int(input("Enter the Search Element :"))
result=l1.search(target)
print("Not found") if result==-1 else print(f"Found the element {target} At {result}")