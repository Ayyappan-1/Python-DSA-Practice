# Merge Sort which has time complexity of O(n log n) and space complexity of O(n)
def merge(a,b):
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


def merge_sort(a):
    l=len(a)-1
    if(len(a)<=1):
        return a
    mid=(len(a))//2
    left=a[:mid]
    right=a[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)

a=[7,3,8,1,0,3,5]
d=[]
d=merge_sort(a)
print(d)
    