# Stack implementation of array. For all the operations, time complexity is O(1) and space complexity is O(n).
# Deleting a element which is in top position.
def pop(top):
    if(top==-1):
        print("Stack Underflow Detected...") 
    else:
        top-=1
    return top

# Pushing/Inserting an element into the stack.
def push (element,top,size):
    if(top+1>=size):
        print("\nStack Overflow Detected...\n")
    else: 
        top+=1
        stack[top]=element
        print("\nInserted successfully\n")
    return top

# Accessing the top element (Last inserted element)
def peek(top):
    if(top==-1):
        print("\nStack Underflow, no elements to display...\n")
        return
    print("\nTop element : ",stack[top],"\n")

# Checking whether the stack is full.
def isfull(top,size):
    if(top+1>=size):
        print("\nStack is full now....\n")
    else:
        print(f"\nStack has {size-(top+1)} spaces for pushing elements...\n")

# Checking whether the stack is empty.
def isempty(top):
    if(top==-1):
        print("\nStack is empty....\n")
    else:
        print("\nStack is not empty....\n")

top=-1
size=4
stack=[0]*size
while(True):
    print("Stack Menu\n1.Push\n2.Pop\n3.Peek\n4.Isempty\n5.Isfull\n6.Exit\n")
    choice=input("Enter the valid choice number :")
    match choice:
        case '1':
            ele=int(input("Enter the elemnent :"))
            top=push(ele,top,size)
        case '2':
            top=pop(top)
        case '3':
            peek(top)
        case '4' :
            isempty(top)
        case '5':
            isfull(top,size)
        case '6':
            break
        case _:
            print("Invalid Choice, enter the valid choice....")
