# Array implementation of queue which has the time complexity of O(1) and space complexity of O(n)
def enqueue(element,front,rear,size):
    if(rear+1>=size):
        print("Queue is full...")
        return front, rear
    if(front==-1):
        front=0
    rear+=1
    queue[rear]=element
    return front, rear

def dequeue(front,rear):
    if(front>rear):
        front,rear=-1,-1
    front+=1
    if(front==-1):
        print("The queue is empty...")
        return front,rear
    return front,rear

def peek(front,rear):
    if(front==-1 ):
        print("The queue is empty...")
        return
    print("The front element is :",queue[front])

def isempty(front,rear):
    if(front==-1 ):
        print("The queue is empty...")
    else:
        print(f"The queue has space for insertion")

def isfull(front,rear):
    if(size==rear+1):
        print("The queue is full...")
    else:
        print(f"The queue has space for insertion")

size=5
queue=[0]*size
front=rear=-1
while(True):
    print("Queue Menu\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Isempty\n5.Isfull\n6.Exit\n")
    choice=input("Enter the valid choice number :")
    match choice:
        case '1':
            ele=int(input("Enter the elemnent :"))
            front,rear=enqueue(ele,front,rear,size)
        case '2':
            front,rear=dequeue(front,rear)
        case '3':
            peek(front,rear)
        case '4' :
            isempty(front,rear)
        case '5':
            isfull(front,rear)
        case '6':
            break
        case _:
            print("Invalid Choice, enter the valid choice....")



