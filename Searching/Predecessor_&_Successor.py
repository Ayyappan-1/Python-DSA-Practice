# Brute Force which has the time complexity of O(n) and space complexity of O(1)
def predecessor_successor(a,target):
    predecessor=successor=-1
    for i in a: 
        if(i<target):
            if(predecessor==-1 or i>predecessor):
               predecessor=i
        if(i>target  ):
            if(successor==-1 or i<successor):
               successor=i
    return predecessor,successor

# Optimized method by using binary search algorithm which has the time complexity of O(log n) and space complexity of O(1)
def optimized(a,target):
    predecessor,successor=float('-inf' ),float("inf")
    low=0
    high=len(a)-1
    while(high>=low):
        mid=(high+low)//2  
        if(a[mid]==target):
            if mid - 1 >= 0:
                pred = a[mid - 1] 
            if mid + 1 < len(a):
                succ = a[mid + 1]
            return pred, succ
        if(a[mid]<target): 
            low=mid+1 
            predecessor=a[mid]
        else:
            high=mid-1 
            successor=a[mid]
    return predecessor,successor

a=[1,2,3,5,6,7,8]
target=int(input("Enter the Target :"))
pre,suc=predecessor_successor(a,target)
print(f"Floor : {pre}\nCeil : {suc}")
p,s=optimized(a,target)
print(p,s)