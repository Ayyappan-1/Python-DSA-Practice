# Brute force method for left rotation which has the time complexity of O(n^2) and space Complexity O(1)
def left_rotation(b,d):
    l=len(b)-1
    for i in range(0,d):
        b.append(None) 
        b[l+1]=b[0]
        b.pop(0)
    return b

# Optimized method by using reversal algorithm which has the time complexity of O(n) and space complexity of O(1)
def optimized(l,r):  
    while(l<r):
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1  

a=[1,2,3,4,5,6,7,8,9]
b=[]
d=int(input("Enter Number of Rotation Needed :")) 
l=len(a)-1
d=d%(l+1)

b=left_rotation(a.copy(),d)
optimized(0,d-1)
optimized(d,l)
optimized(0,l)
print("Brute Force Method : ",b)
print("Optimized Method : ",a)