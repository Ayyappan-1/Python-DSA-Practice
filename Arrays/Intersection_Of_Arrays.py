# Brute force method which has the time complexity of O(n x m) and Space complexity of O(k)
def array_intersection(a,b):
    c=[]
    for i in range(0,len(a)):
        if(a[i] in b and a[i] not in c):
            c.append(a[i])
    return c

# Optimized Hash Based Algorithm which has the time complexity of O(n) and Space complexity of O(m)
def optimized(a,b):
    s=set()
    d=[]
    for i in a:
        if(i not in s):
            s.add(i)
    for i in b:
        if(i in s):
            d.append(i)
            s.remove(i)
    return d

c,d=[],[]
a=list(map(int,input("Enter Elements of A :").split()))
b=list(map(int,input("Enter Elements of B :").split()))
c=array_intersection(a.copy(),b.copy())
print("Brute Force Method :",c)
d=optimized(a.copy(),b.copy())
print("Optimized Method :",d)