#Removing Duplicates by a another list which has O(n^2)
def duplicate_removal(a):
    b=[]
    for i in a: 
        if(i not in b):
            b.append(i)
    print("List Adding Method :",b)
 
#Optimized method by using a set for tracking elements and avoid duplicats which has O(n)
def optimized(a):
    b=set()
    c=[]
    for i in a:
        if(i not in b):
            b.add(i)
            c.append(i)
    print("Optimized Method :",c)

a=[1,2,3,1,7,2,7,1]
duplicate_removal(a)
optimized(a)