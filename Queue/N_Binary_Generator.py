# Printing binary values for N numbers by using queue which has the time complexity of O(n)  and space complexity of O(n)
def enqueue(element,front,rear,size):
    if(rear+1>=size):
        print("Queue is full...")
        return front, rear
    if(front==-1):
        front=0
    rear+=1
    queue[rear]=element
    return front, rear


def dequeue(front,rear,size):
    if(front>rear):
        return -1,-1,None
    popped=queue[front]
    front+=1
    return front,rear, popped


def generator(n,front,rear,size):
    front,rear=enqueue('1',front,rear,size)
    for _ in range(n):
        front,rear,popped=dequeue(front,rear,size)
        if(popped==None):
            return 
        print(popped)
        front,rear=enqueue(popped+'0',front,rear,size)
        front,rear=enqueue(popped+'1',front,rear,size)

n=int(input("Enter the number :"))
size=(2*n+5)
queue=[None]*size
generator(n,-1,-1,size)