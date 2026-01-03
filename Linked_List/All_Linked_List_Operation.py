class Node:
    def __init__(self, data):
        self.data=data 
        self.next= None

class Linked_List :
    def __init__(self):
        self.head=None
        self.size=0

    def insert_at_head(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
        self.size+=1

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
    
    def insert_at_tail(self,data):
        new_node=Node(data)
        if self.head!=None :
           current_node=self.head
           while current_node.next !=None:
               current_node=current_node.next
           current_node.next=new_node
        else:
            self.head=new_node
        self.size+=1

            
    def deletion_at_head(self):
        current=self.head
        if(self.size>0):
            self.head=current.next
            current.next=None
            self.size-=1
        else:
            print("Linked List Is Empty....")

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

    def delete_at_tail(self):
        if(self.head==None):
            print("Nothing to delete, Linked list is Empty !")
            return
        current_node=self.head
        if(current_node.next==None):
            self.head=None
            self.size-=1
            return
        while(current_node.next.next!=None): 
            current_node=current_node.next
        current_node.next=None
        self.size+=1
    def display(self):
        current=self.head 
        i=0
        while self.size>i:
            print(current.data)
            current=current.next
            i+=1

l1=Linked_List()
while(True):
    print("Linked List Menu.....\n1.Insert at head \n2.Insert at position\n3.Insert at tail\n4.Delete at head\n5.Delete at position\n6.Delete at tail\n7.Display\n8.End\n")
    ans=input("Enter the valid choice number :")
    match ans:
        case '1' : 
            inp=int(input("Enter the number to insert :"))
            l1.insert_at_head(inp)
        case '2':
            inp=int(input("Enter the number to insert :"))
            pos=int(input("Enter the position to insert :"))
            l1.insert_at_position(inp,pos)
        case '3':
            inp=int(input("Enter the number to insert :"))
            l1.insert_at_tail(inp)
        case '4':
            l1.deletion_at_head()
        case '5':
            pos=int(input("Enter the position to delete :"))
            l1.delete_at_position(pos)
        case '6':
            l1.delete_at_tail()
        case '7':
            l1.display()
        case '8':
            break
