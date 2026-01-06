# Linked List implementation of queue which has the time complexity of O(1) and space complexity of O(n)
class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
 
class Queue:
    def __init__(self):
        self.front=None 
        self.rear=None

    def enqueue(self,element):
        new_node=Node(element)
        if(self.front==None):
            self.rear=new_node
            self.front=new_node
        else:
            self.rear.next=new_node
            self.rear=self.rear.next
    
    def dequeue(self):
        if(self.front==None):
            print("The queue is empty...")
            return
        if(self.rear==self.front):
            self.rear=self.front=None 
            return
        current_node=self.front
        self.front=self.front.next
        current_node.next=None
        
    def peek(self):
        if(self.front==None):
            print("Queue is empty...")
            return
        print("The front element is :",self.front.data)

    def isempty(self):
        if(self.front==None):
            print("Queue is empty...")
        else:
            print("Queue is not empty")
 
q1=Queue()
while(True):
    print("Queue Menu\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Isempty\n5.Exit\n")
    choice=input("Enter the valid choice number :")
    match choice:
        case '1':
            ele=int(input("Enter the elemnent :"))
            q1.enqueue(ele)
        case '2':
            q1.dequeue( )
        case '3':
            q1.peek( )
        case '4' :
            q1.isempty( )
        case '5':
            break
        case _:
            print("Invalid Choice, enter the valid choice....")





