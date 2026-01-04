# Stack implementation of Linked List. For all operations, the time complexity is O(1) and space complexity is O(n)
# Node class is to create N number of nodes necessary for our stack and each node is considered to be a object of node..
class Node :
    def __init__(self,data):
        self.data=data
        self.next=None

# Stack is is the heart and responsible for creation of a linked list based stack and assigning head reference with all other operations.
class Stack:
    def __init__(self):
        self.top=None 

    def push(self,data):
        next_node=Node(data)
        next_node.next=self.top
        self.top=next_node 
 
    def pop(self):
        if(self.top==None):
            print("Stack underflow is detected.")
        else:
            current=self.top 
            self.top=current.next
            current.next=None 
         

    def peek(self):
        if(self.top!=None):
            print("Top element :",self.top.data)
        else:
            print("Stack Underflow detected.")

    def isempty(self):
        if(self.top==None):
            print("Yes, Stack is empty")
        else :
            print(f"No, stack has elements")
 
s1=Stack()
while(True):
    print("Stack Menu\n1.Push\n2.Pop\n3.Peek\n4.Isempty\n5.Exit\n")
    choice=input("Enter the valid choice number :")
    match choice:
        case '1':
            ele=int(input("Enter the elemnent :"))
            s1.push(ele)
        case '2':
            s1.pop()
        case '3':
            s1.peek()
        case '4' :
            s1.isempty()
        case '5':
            break
        case _:
            print("Invalid Choice, enter the valid choice....")
