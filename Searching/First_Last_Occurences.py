# Brute Force method which uses time complexity of O(n) and space complexity of O(1)
def first_last_occurence(a,tar):
    first=last=-1
    for i in range(len(a)):
        if(tar==a[i] and first==-1):
            first=i
        if(tar==a[i]):
            last=i
    return first,last

# Optimized Method which uses binary search which has the time complexity of O(log n) and space complexity of O(1)
def binary_search(a,target,search_place):
    low=0
    found=-1
    high=len(a)-1
    while(high>=low):
        mid=(high+low)//2
        if(a[mid]==target):
            if(search_place=='first'):
              high=mid-1
            else:
                low=mid+1
            found=mid 
        elif(a[mid]>target):
            high=mid-1
        else:
            low=mid+1
    return found

a=[1,2,3,4,6,7,9]
tar=3

f,l=first_last_occurence(a,tar)
print("Brute Force :-")
if(f==-1):
    print("The target does not found...")
elif(f==l):
    print("The target element is occured only once at :",f)
else:
    print(f"The first occurence is at {f} and second occurence is at {l}")


first=binary_search(a,tar,'first')
last=binary_search(a,tar,'last')
print("\nOptimized Method :-")
if(first==-1):
    print("The target does not found...")
elif(first==last):
    print("The target element is occured only once at :",first)
else:
    print(f"The first occurence is at {first} and second occurence is at {last}")
