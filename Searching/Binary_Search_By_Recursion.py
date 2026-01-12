# Binary search by recursion method which has the time complexity of O(log n) and space complexity of O(log n)
def binary_search(a,l,r,target):
    if(l>r):
        return False 
    mid=(l+r)//2
    if(target==a[mid]):
        return True
    elif(target>a[mid]): 
        return binary_search(a,mid+1,r,target)
    else: 
        return binary_search(a,l,mid-1,target)

a=[1,2,4,5,7,8,9]
target=int(input("Enter the number to search :"))
res=binary_search(a,0,len(a)-1,target)
print("Yes, the element is present...") if res else print("No, the element does not present in the list...")