# Quick Sort by Lomuto Partition Scheme (functional version) which has the time complexity of worst case -> O(n^2), average and best case ->O(n log n) and the space complexity is O(n)
def quick_sort(a):
    if(len(a)<=1):
        return a
    pivot=len(a)-1
    i=-1
    for j in range(pivot): 
        if(a[j]<=a[pivot]):
            i+=1
            if(a[i]>a[j]):
                a[j],a[i]=a[i],a[j]
    i+=1
    a[i],a[pivot]=a[pivot],a[i]
    pivot=i
    left=quick_sort(a[:pivot])
    right=quick_sort(a[pivot+1:])
    return left+[a[pivot]]+right

a=[7,5,2,0,6,1,2,9,-3,-1]
a=quick_sort(a)
print(a)
        
