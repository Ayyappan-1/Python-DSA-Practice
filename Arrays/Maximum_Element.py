def maximum():
    max=a[0]
    for i in range(len(a)-1):
        if(max<a[i+1]):
            max=a[i+1]
    return max

a=[1,2,9,0,12,43,0]
max=maximum()
print(max)
