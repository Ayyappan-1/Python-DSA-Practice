# Brute Force appraoch which takes the time complexity of O( (n+m) log (n+m) ) and Space complexity of O(n+m)
def merge_array(a,b):
    c=[]
    c.extend(b)
    c.extend(a)
    c.sort()
    return c
    
# Two pointer based optimization which has the time coplexity of O(n+m) and Space complexity of O(n+m)
def optimized(a,b):
    d=[]
    i,j=0,0
    while(i<=len(a)-1 and j<=len(b)-1):
        if(a[i]< b[j]):
            d.append(a[i])
            i+=1
        elif(a[i]==b[j]):
            d.append(a[i])
            d.append(b[j])
            i+=1
            j+=1
        else:
            d.append(b[j])
            j+=1
    for k in range(j,len(b)):
        d.append(b[k])
    for l in range(i,len(a)):
        d.append(a[l])
    return d

c,d=[],[]
a=list(map(int,input("Enter Elements of A :").split()))
b=list(map(int,input("Enter Elements of B :").split()))
c=merge_array(a,b)
print("Brute Force Method :",c)
d=optimized(a,b)
print("Optimized Method :",d)