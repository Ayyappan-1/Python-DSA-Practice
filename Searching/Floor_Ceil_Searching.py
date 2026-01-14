# Brute Force which has the time complexity of O(n) and space complexity of O(1)
def floor_ceil(a,target):
    floor=ceil=-1
    for i in a:
        if(i==target):
            return i,i
        if(i<target):
            if(floor==-1 or i>floor):
               floor=i
        if(i>target and ceil==-1):
            if(ceil==-1 or i<ceil):
               ceil=i
    return floor,ceil
# Optimized method by using binary search algorithm which has the time complexity of O(log n) and space complexity of O(1)
def optimized(a,target):
    floor,ceil=float('-inf' ),float("inf")
    low=0
    l=high=len(a)-1
    while(high>=low):
        mid=(high+low)//2 
        if(a[mid]==target):
            return a[mid],a[mid]
        
        if(a[mid]<target): 
            low=mid+1 
            floor=max(a[mid],floor)
        else:
            high=mid-1 
            ceil=min(a[mid],ceil)
    return floor,ceil
# Optimized Method by binary search algorithm which has the time complexity of O(log n) and space complexity O(1)

a=[1,2,3,5,6,7,8]
target=4
floor,ceil=floor_ceil(a,target)
print(f"Floor : {floor}\nCeil : {ceil}")
f,c=optimized(a,target)
print(f,c)