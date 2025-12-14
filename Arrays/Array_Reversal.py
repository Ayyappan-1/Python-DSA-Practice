a=[1,2,3,4,5,6,7,8]
l=len(a)
le=l-1
for i in range(0,l//2):
    temp=a[i]
    a[i]=a[le]
    a[le]=temp
    le-=1
    print(a,i)
     