# Finding Lenght and Middle element of a linked list at the same program which has the time complexity of O(n) and Space complexity of O(1)
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

    def middle_element(self):
        current_node=self.head
        length=self.length()
        if(length==0):
            print("There is no element to find middle element......")
        mid=length//2 
        i=0
        while (i<mid):
            current_node=current_node.next
            i+=1
        print("Middle Element :",current_node.data)

    def length(self):
        current_node=self.head
        l=0
        while(current_node!=None):
            current_node=current_node.next
            l+=1 
        return l
    
# Slow-Fast Pointer method which decreases the operational cost then brute force even though it is O(n) [same as brute force]
    def optimized(self):
        slow_pointer=fast_pointer=self.head
        if(self.head==None):
            print("There is no element to find middle element......")
            return
 
        while(fast_pointer!=None and fast_pointer.next!=None):
             fast_pointer=fast_pointer.next.next
             slow_pointer=slow_pointer.next
        print("slow-fast pointer :",slow_pointer.data)

l1=Linked_List()
l1.insert_at_head(30)
l1.insert_at_head(20)
l1.insert_at_head(5) 
l1.insert_at_head(2) 
l1.middle_element()
l1.optimized()