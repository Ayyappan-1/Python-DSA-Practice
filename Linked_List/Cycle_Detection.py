# Finding cycles of a linked list which has the time complexity of O(n) and Space complexity of O(n)
class Node:
    def __init__(self, data):
        self.data=data 
        self.next= None
class Linked_List :
    def __init__(self):
        self.head=None

    def insert_at_head(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node

    def cycle_finder(self):
        current_node=self.head
        b=set()
        if(current_node==None):
                print("Linked List is Empty")

        while(current_node!=None): 
            if(current_node not in b):
                b.add(current_node)
            else:
                return current_node.data
            current_node=current_node.next
        return -1
    
# Optmimized method uses slow-fast pointer alogrithm which has time complexity of O(n) and space compelxity of O(1)
    def optimized(self):
        slow=fast=self.head
        while (fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(fast==slow):
                return True
        return False 
            
    def display(self):
        current=self.head 
        while current!=None:
            print(current.data)
            current=current.next
            
l1=Linked_List()
l1.insert_at_head(10)
l1.insert_at_head(20)
l1.insert_at_head(30)
l1.insert_at(40)
result=l1.cycle_finder()
print("Brute Force : There is a cycle :",result) if(result!=-1) else print("Brute Force : There is no such cycle exist....")
answer=l1.optimized()
print("Optimized : There is a cycle") if(answer==True) else print("Optimized : There is no such cycle exist")
            