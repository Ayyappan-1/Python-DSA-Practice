# Brute force method for right rotation which has the time complexity of O(n x d) --> O(n^2) and space Complexity O(1)
def right_rotation(b,d):
    l=len(b)-1
    for i in range(0,d):
        b.insert(0,None) 
        b[0]=b[l+1]
        b.pop(l+1)
    return b

# Optimized method by using reversal algorithm which has the time complexity of O(n) and space complexity of O(1)
def optimized(l,r):  
    while(l<r):
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1  

a=[1,2,3,4,5,6,7,8,9]
b=[]
d=int(input("Enter Number of Right Rotation Needed :")) 
l=len(a)-1
d=d%(l+1)

b=right_rotation(a.copy(),d)
optimized(0,l)
optimized(0,d-1)
optimized(d,l)

print("Brute Force Method : ",b)
print("Optimized Method : ",a)