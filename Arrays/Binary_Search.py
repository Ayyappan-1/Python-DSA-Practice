# Binary Search Algorithm which has O(log n)
def binary_search(a,target):
    low=0
    l=high=len(a)-1
    for i in range(high+1):
        mid=(high+low)//2
        if(a[mid]==target):
            return mid
        elif(a[mid]>target):
            high=mid-1
        else:
            low=mid+1
    return -1

a=[1,2,3,7,10,34,56]
target=int(input("Enter the target element :"))
index=binary_search(a,target)
print("The target not found.....") if index==-1 else print(f"The targe element found at [{index+1}] position...")
